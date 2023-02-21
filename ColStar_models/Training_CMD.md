For the training of a Col$\star$ model, `cd` the folder of the model, you can using the following command:

 
If you would like to train a model with Cosine similarity function, please use the following command:

```python
python -m colbert.train --amp --doc_maxlen 180 --mask-punctuation --bsize 32 --accum 1 --triples /path/to/triples.train.small.tsv --root /path/to/save/model/ColBERT/ --experiment psg --run ColBERT_cosine--similarity cosine
```


Similarly, if you would like to train a model with L2 similarity function, using this:

```python
python -m colbert.train --amp --doc_maxlen 180 --mask-punctuation --bsize 32 --accum 1 --triples /path/to/triples.train.small.tsv --root /path/to/save/model/ColBERT/ --experiment psg --run ColBERT_l2 --similarity l2
```