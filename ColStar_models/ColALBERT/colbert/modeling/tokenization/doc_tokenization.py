import torch

# from transformers import XLMRobertaTokenizer
from transformers import AlbertTokenizer
from colbert.modeling.tokenization.utils import _split_into_batches, _sort_by_length


class DocTokenizer():
    def __init__(self, doc_maxlen):
#         self.tok = AlbertTokenizer.from_pretrained('albert-base-v2')
        # now train colalbert using albert-xxlarge-v2
#         self.tok = AlbertTokenizer.from_pretrained('albert-large-v2')
        self.tok = AlbertTokenizer.from_pretrained('albert-base-v2')
#         self.base_model = base_model
#         self.tok = AlbertTokenizer.from_pretrained(self.base_model)
        self.tok.add_tokens(['[unused0]'])
        self.tok.add_tokens(['[unused1]'])
        self.doc_maxlen = doc_maxlen

        self.D_marker_token, self.D_marker_token_id = '[D]', self.tok.convert_tokens_to_ids('[unused1]') 
        self.cls_token, self.cls_token_id = self.tok.cls_token, self.tok.cls_token_id
        self.sep_token, self.sep_token_id = self.tok.sep_token, self.tok.sep_token_id

        # assert self.D_marker_token_id == 50262

    def tokenize(self, batch_text, add_special_tokens=False):
        assert type(batch_text) in [list, tuple], (type(batch_text))

        tokens = [self.tok.tokenize(x, add_special_tokens=False) for x in batch_text]

        if not add_special_tokens:
            return tokens

        prefix, suffix = [self.cls_token, self.D_marker_token], [self.sep_token]
        tokens = [prefix + lst + suffix for lst in tokens]

        return tokens

    def encode(self, batch_text, add_special_tokens=False):
        assert type(batch_text) in [list, tuple], (type(batch_text))

        ids = self.tok(batch_text, add_special_tokens=False)['input_ids']

        if not add_special_tokens:
            return ids

        prefix, suffix = [self.cls_token_id, self.D_marker_token_id], [self.sep_token_id]
        ids = [prefix + lst + suffix for lst in ids]

        return ids

    def tensorize(self, batch_text, bsize=None):
        assert type(batch_text) in [list, tuple], (type(batch_text))

        # add placehold for the [D] marker
#         batch_text=["do goldfish grow"]
        batch_text = ['. ' + x for x in batch_text]
#         print(">>>doc_tokenization.py tensorize: first doc length",len(batch_text[0]),"\n",batch_text[0])

        obj = self.tok(batch_text, padding='longest', truncation='longest_first',
                       return_tensors='pt', max_length=self.doc_maxlen)

        ids, mask = obj['input_ids'], obj['attention_mask']
#         print(">>>doc_tokenization.py tensorize: first len dids:",len(ids[0]))
#         print(">>>doc_tokenization.py tensorize: first ids:",ids[0])
#         print(">>>doc_tokenization.py tensorize: first mask len:", len(mask[0]))

        # postprocess for the [D] marker
        ids[:, 1] = self.D_marker_token_id

        if bsize:
            ids, mask, reverse_indices = _sort_by_length(ids, mask, bsize)
            batches = _split_into_batches(ids, mask, bsize)
            return batches, reverse_indices

        return ids, mask
