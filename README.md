# ColStar 
Virtual Appendix for Xiao Wang, Craig Macdonald, Nicola Tonellotto, Iadh Ounis. Reproducibility, Replicability, and Insights into Dense Multi-Representation Retrieval Models: from ColBERT to Col*. In Proceedings of SIGIR 2023.


# Training 
For Training and Indexing a Col* model, please follow this [instruction for training](ColStar_models/Training_CMD.md).
The trained checkpoints for the selected Col* models, namely ColBERT-Cosine, ColBERT-L2, ColRoBERTa and ColALBERT, to build the dense index are shared here: https://drive.google.com/drive/folders/1S9d1M_5LGcGyC6W15ZOCL6KGGRNc6wXa?usp=sharing

# Indexing

Using your own trained model or our shared checkpoint, you can build the dense index following this [instruction for indexing](ColStar_models/index.md).




# Evaluation 

## Reproducibility Experiments
We first conduct the reproducibility study of ColBERT, by training our own ColBERT model. The reproducibility experiments are demonstrated in this [demo notebook](Reproducibility%20(RQ1%20Res)/Reproducibility_Demo%20(RQ1%20results).ipynb). In addition, all the results files are provided under this [Reproducibility results folder](Reproducibility%20(RQ1%20Res)/).
Based on the results of our reproducibility study, we conclude that we can well-reproduce the training of ColBERT.

## Replicability Experiments
Then, based on the success of our reproducibility study, we further conduct the replicability study where we extend the ColBERT to Col*. In particular, Col* is a collection of models where we implement the Contextualised Late Interaction Mechanism upon various underlying Pretrained Language Models with different tokenisers. 
The replicability experiments of our paper are demonstrated in this [demo notebook](Replicability%20(RQ2%20Res)/Replicability_Demo%20(RQ2%20results).ipynb). Also, all the results files that can be used to reproduce our results are provided in this [Replicability results folder](Replicability%20(RQ2%20Res)/).

Based on the results of our replicability study, we conclude that we can replicate the contextualised late interaction mechanism upon various pretrained models. Moreover, in the following, we report the statistics of four selected Col* models that are built upon the base-size PLM but with different tokenisers, namely ColBERT, ColminiLM, ColRoBERTa and ColALBERT models.
<img width="976" alt="image" src="https://github.com/Xiao0728/ColStar_VirtualAppendix/assets/43675140/a4d53794-e51a-4cb7-b5fd-f13fde9b9050" width="20%" height="10%" >




## Insights Experiments

Furthermore, we investigate the matching behaviour of our selected Col* models to obtain more insights. In particular, we investigate the following research questions:
- How does the late interaction matching behaviour varies across different Col* models?
- How does the Col* models impact on the matching bebavaiour across different types of tokens?
- Can we quantify the contribution of different types of matching behaviour?

In particular, according to the following experiment results, we find that (i) ColRoBERTa is more likely to perform semantic matching than other models **(RQ1)**; (ii) Low IDF tokens are most likely to exhibit semantic matching  **(RQ2)**; (iii) Col* modelsbenefit more from lexical matching than semantic matching, less so for ColRoBERTa! Please check more results in our paper!
.
<img width="500" alt="image" src="https://github.com/Xiao0728/ColStar_VirtualAppendix/assets/43675140/0cecc961-58eb-4ca5-939f-ce09c3482d86">


To reproduce the above results, we also provide a demo [demo notebook](Insights%20(RQ3%20Res)/ColStar_SMP_Demo%20(RQ3%20Res).ipynb) for the insights experiments.
Or, instead of running the experiments from scratch, you can use our provided results files in this [Insights results folder](Insights%20(RQ3%20Res)/) directly to reproduce our presented results.


# Reference
[Wang23]: Xiao Wang, Craig Macdonald, Nicola Tonellotto, Iadh Ounis. Replicability, and Insights into Dense Multi-Representation Retrieval Models: from ColBERT to Col*. In Proceedings of SIGIR 2023.
