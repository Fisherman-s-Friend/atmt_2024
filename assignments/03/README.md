# Assignment 3: Improving Low-Resource NMT

In this assignment we use fr-en data from the Tatoeba
corpus and investigate methods for improving low-resource NMT.

Your task is to experiment with techniques for improving
low-resource NMT systems.

## Baseline

The data used to train the baseline model was prepared using
the script `preprocess_data.sh`.
This may be useful if you choose to apply subword
segmentation or a data augmentation method.

# Code adaptions

We modified preprocess.py named it preprocess_new.py to implement BPE, as well as additionally created tokenizer.py to use for BPE and an detokenizer,.py which was not used for the assignment but would solve our spacing problem mentioned in the report.
