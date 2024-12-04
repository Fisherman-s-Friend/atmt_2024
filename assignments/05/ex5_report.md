# ATMT Exercise 5

Jana Hofmann & Dominic Fischer

## 1. Experimenting with Beam Search

![Bleu scores for different Beam sizes.](bleu_scores.png)

In terms of BLEU scores, we see the trend that we would have expected: a bigger beam size leads to better translations, but only up to a certain point. After that, we start to overly favour high-probability sequences, diminishing variability in the translation (this is bad, natural language is not deterministic, we need a certain variability). The best BLEU score of 22.7 is achieved with a beam size of 13, afterwards, performance drops slightly and seems to remain slightly below a BLEU score of 22. It is to be noted that if we increase the beam size by one and notice a drop in performance, we should not stop immediately. Rather, do the same thing for the next or maybe even the next two beam sizes. If these then also show a lower performance, we know that we have surpassed the zenith and therefore know which is the best beam size.

Interestingly, the brevity penalty drops (= the translations get shorter) as the beam size increases. We explain this as follows: the more we increase the beam size, the more emphasis we put on high probability. Tokens probabilities are chained together and, because they are mostly less than one, the longer a sequence, the less probable. Therefore, shorter sequences are favoured. Furthermore, language tends to favour short tokens for reasons of economy, thus short tokens are more probable and will also be favoured by the model.
