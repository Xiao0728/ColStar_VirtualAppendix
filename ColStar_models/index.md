After obtaining a trained checkpoint, you can build the index for a Col$\star$ model using the following code.

```python
import sys
import faiss
import pyterrier as pt
pt.init()
import pyterrier_colbert.indexing
from pyterrier_colbert.indexing import ColBERTIndexer
import colbert.indexing.faiss
colbert.indexing.faiss.SPAN = 1
index_root="/path/to/index_root/"
index_name="msmarco_passage_index_colstar"
dataset = pt.get_dataset("irds:msmarco-passage")
indexer = ColBERTIndexer("/path/to/checkpoints/colbert-xxx.dnn", index_root,  index_name, chunksize=3)
indexer.index(dataset.get_corpus_iter())
```
    
    

