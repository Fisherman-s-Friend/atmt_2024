# ATMT Exercise 5

Jana Hofmann & Dominic Fischer

## 1. Experimenting with Beam Search

![Bleu scores for different Beam sizes.](bleu_scores.png)

In terms of BLEU scores, we see the trend that we would have expected: a bigger beam size leads to better translations, but only up to a certain point. After that, we start to overly favour high-probability sequences, diminishing variability in the translation (this is bad, natural language is not deterministic, we need a certain variability). The best BLEU score of 22.7 is achieved with a beam size of 13, afterwards, performance drops slightly and seems to remain slightly below a BLEU score of 22. It is to be noted that if we increase the beam size by one and notice a drop in performance, we should not stop immediately. Rather, do the same thing for the next or maybe even the next two beam sizes. If these then also show a lower performance, we know that we have surpassed the zenith and therefore know which is the best beam size.

Interestingly, the brevity penalty drops (= the translations get shorter) as the beam size increases. We explain this as follows: the more we increase the beam size, the more emphasis we put on high probability. Tokens probabilities are chained together and, because they are mostly less than one, the longer a sequence, the less probable. Therefore, shorter sequences are favoured. Furthermore, language tends to favour short tokens for reasons of economy, thus short tokens are more probable and will also be favoured by the model.

## 2. Understanding the Code

cf. "translate_beam.py".

## 3. Exploring Stopping Criteria in Beam Search

### 3.1 Understanding the current stopping condition

The "add_final" function in "beam.py" (row 24) is responsible for putting  a finished sequence on to the queue of final hypotheses, after having padded it to make sure all hypotheses have the same length. It is called in row 193 in "translate_beam.py" if the last index is the EOS-token, which means that that hypothesis is done.

The beam size is reduced as "translate_beam.py" (row 216) calls "prune" in "beam.py" (row 57). There, we reassign our nodes-to-be-expanded-stack, putting only the top #beam_size-finished nodes onto the stack. In terms of why this should make sense, I would explain it as follows:

- we start from the k most probable translations and pursue them
- Once one of these is done, we know that we have found one of the k most probable translations, so we just need to look for the remaining k-1.

### 3.2 Implementing a Constant Beam Size Stopping Criterion

For this, we alter the "prune" function in "beam.py", row 57. Instead of changing the effective beam size by truncating the queue of unfinished nodes at #beam_size-finished (old "prune" function, row 62), we keep said queue at a max of length beam_size (row 75) and only move nodes from there to the finished queue if they reach the max length (row 72).

The BLEU score (19.1) and its split was exactly the same, meaning also all the chosen translations were the same. The times, however, were very different. The original method took only 21 seconds, while the modified method took 6 minutes and 22 seconds. Based on this experiment, keeping the beam size does not make sense at all. We end up with a bunch of overly long and therefore unlikely translations, and the one that would be chosen with a changing beam is chosen anyways.

### 3.3 Implementing a Stopping Criterion with Pruning