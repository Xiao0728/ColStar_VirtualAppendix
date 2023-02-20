import string
import torch
import torch.nn as nn


# from transformers import RobertaPreTrainedModel, RobertaConfig, RobertaModel, RobertaTokenizer
from transformers import AlbertForPreTraining, AlbertModel, AlbertTokenizer

from colbert.parameters import DEVICE


class ColBERT(AlbertForPreTraining):
    # config_class = RobertaConfig

    def __init__(self, config, query_maxlen, doc_maxlen, mask_punctuation, dim=128, similarity_metric='cosine'):

        super(ColBERT, self).__init__(config)
        print(config)
       

        self.query_maxlen = query_maxlen
        self.doc_maxlen = doc_maxlen
        self.similarity_metric = similarity_metric
        self.dim = dim

        self.mask_punctuation = mask_punctuation
        self.skiplist = {}
        # now train colalbert using albert-base-v2
#         self.tokenizer = AlbertTokenizer.from_pretrained('albert-base-v2')
        # now train colalbert using albert-xxlarge-v2
#         self.tokenizer = AlbertTokenizer.from_pretrained('albert-large-v2')
        self.tokenizer = AlbertTokenizer.from_pretrained('albert-base-v2')
#         self.tokenizer = AlbertTokenizer.from_pretrained(self.base_model)
        self.tokenizer.add_tokens(['[unused1]'])
        self.tokenizer.add_tokens(['[unused2]'])
        
        self.albert = AlbertModel(config)
#         self.colbert = AlbertModel(config)
#         self.albert.resize_token_embeddings(len(self.tokenizer)) 

        self.linear = nn.Linear(config.hidden_size, dim, bias=False)

        self.init_weights()

    def forward(self, Q, D):
        return self.score(self.query(*Q), self.doc(*D))

    def query(self, input_ids, attention_mask):
        input_ids, attention_mask = input_ids.to(DEVICE), attention_mask.to(DEVICE)
        Q = self.albert(input_ids, attention_mask=attention_mask)[0]
        Q = self.linear(Q)

        return torch.nn.functional.normalize(Q, p=2, dim=2)

    def doc(self, input_ids, attention_mask, keep_dims=True):
        input_ids, attention_mask = input_ids.to(DEVICE), attention_mask.to(DEVICE)
        D = self.albert(input_ids, attention_mask=attention_mask)[0]
        D = self.linear(D)

        mask = torch.tensor(self.mask(input_ids), device=DEVICE).unsqueeze(2).float()
        D = D * mask

        D = torch.nn.functional.normalize(D, p=2, dim=2)

        if not keep_dims:
            D, mask = D.cpu().to(dtype=torch.float16), mask.cpu().bool().squeeze(-1)
            D = [d[mask[idx]] for idx, d in enumerate(D)]

        return D

    def score(self, Q, D):
        if self.similarity_metric == 'cosine':
            return (Q @ D.permute(0, 2, 1)).max(2).values.sum(1)

        assert self.similarity_metric == 'l2'
        return (-1.0 * ((Q.unsqueeze(2) - D.unsqueeze(1))**2).sum(-1)).max(-1).values.sum(-1)

    def mask(self, input_ids):
        mask = [[(x not in self.skiplist) and (x != 0) for x in d] for d in input_ids.cpu().tolist()]
        return mask
