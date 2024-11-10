
# 1. Neural Machine Translation (NMT)

### a) Evaluation in NMT
**False:** During training and evaluation of an NMT system, only one translation is typically regarded as the target 
(or "gold standard") translation to which the output is compared. Both of these approaches cannot account for the fact 
that there are multiple valid translations for a given source sentence. 
It is a challenge to create an automatic evaluation metric which can take into account multiple valid translation. COMET 
is one doing it, but I don't know about any metric which could be used during training to take that into account.

### b) Disambiguation
**False:** NMT models are capable of disambiguating homographs through context-aware embeddings. 
Additionally, positional encoding in transformers enables the model to distinguish the meaning even based on is 
position in a sequence.

### c) Length Normalization
**True:** Length normalization aims to discourage a model from producing overly short sentences by dividing 
the translation cost by its length. 

---

# 2. Language Representation

### a) Word Representation
Input words are represented by a **numerical index** corresponding to their position in the vocabulary. 
These indices are embedded into **vector representations** of a predefined length, 
which are then passed through the neural network. To produce output words, the manipulated vectors are passed through 
a **softmax function**, generating a probability distribution over the target vocabulary. 
The word corresponding to the highest probability is selected (or used in more sophisticated decoding strategies like beam search, sampling, ...).

### b) Vocabulary Size and Complexity
The larger the vocabulary, the higher the **computational complexity**, as the model must handle a greater number 
of potential outputs during both training and inference.

---

# 3. Seq-to-Seq Models

### a) Language Modeling
Language modeling involves predicting the probability of word sequences. For example, given an English training corpus, 
it might predict that *"The cat eats a fish"* is more probable than *"Dreamed snail penguin yellowish."* 
In translation, we maximize the probability of the target sequence while ensuring it aligns with the meaning of the source sentence.
The **encoder** captures the source sentence's meaning, and the **decoder** generates a probable sequence in the target language.

### b) Non-Seq-to-Seq Tasks
In tasks like text classification, a seq-to-seq model is unnecessary. For instance, in **text classification**, 
the model processes the entire input text and outputs a single label, such as "spam" or "not spam."

---

# 4. Open Vocabulary Translations

### a) Subword-Level NMT
Before subword-level NMT, input was treated as a sequence of words, and each word needed a separate vocabulary entry. 
This leads to multiple challenges: How do we create a vocabulary with all possible words of a language, and if we were to 
succeed in this, how would we handle this large vocab computationally.
Subword-level approaches (e.g., Byte-Pair Encoding) solves this by split words into 
smaller units, enabling the model to handle unknown words by recombining known subwords and therefor enables to encode a 
potentially infinte vocabulary of a language via a finite set of subword tokens.

This posed challenges for rare or unseen words. 
### b) Advantages of Smaller Subword Vocabularies
A smaller subword vocabulary ensures more versatile subword units, 
increasing the likelihood of covering unknown words by combining subwords from the vocabulary.

---

# 5. NMT Architectures

### a) Gate Mechanisms
Gates control how much influence the previous hidden state has on the current hidden state. 
They typically use activation functions like **tanh** (range: [-1, 1]) or **sigmoid** (range: [0, 1]). 
These functions modulate the flow of information, with smaller values reducing the influence and larger values increasing it.

### b) Transformer Blocks
1. **Positional Encoding:** Adds positional information to tokens since transformers process the entire input sequence simultaneously.
2. **Self-Attention:** Computes attention between tokens by generating key, query, and value vectors for each token. 
The resulting scores weight the token representations accordingly.

### c) Masking in Decoders
Removing decoder masking provides the model with future tokens during training, artificially improving cross-entropy scores. 
However, during inference, where tokens are generated sequentially, this results in degraded performance and poor generalization.

---


# 6. Improving Translation Quality

### a) Auto-Encoding and Back-Translation
In most settings of NMT, we have a limited corpus of translations from a source to a target language. 
However, it is typically easier to obtain monolingual data for either the source or target language. 
This motivates leveraging monolingual data to improve the translation system.

One approach is to combine **auto-encoding** with machine translation. 
Here, the model is assigned an additional task: 
reconstructing the source sentence token by token. This reconstruction may involve, for instance, 
shifting the sequence by one time step. By doing so, the model enhances its ability to capture the underlying structure of the source language during encoding.

**Backtranslation** leverages the model's ability to translate a target language back into the source language. 
This method helps generate synthetic parallel data. Often, NMT models perform better when translating from any language
into English rather than vice versa, especially when English serves as a higher-resource language. 
Back translation exploits this by generating more translation pairs using the lower-resource language sentence as input and producing its English translation.

### b) Multilingual NMT
Multilingual models leverage data from multiple languages. This can be used in different ways: 
one possibility is to use a second source language to **disambiguate** the meaning of a token. 
For example, consider the French word banque. Its translation into German could either be Bank or Ufer (depending on the context). 
However, if the English translation is bord (referring to shore), the system can infer that the correct German equivalent is Ufer.
Another possibility is to create unseen language translation pairs by using pivot languages and backtranslation.
For example given the language pairs: {span - engl, engl - fr}, we could create automatically a backtranslation of the 
eng sentences of the engl-fr  pair into span, which than can be used to train a span-fr model. 

### c) Multi-Source, Many-to-one NMT and Massively Multilingual Systems

| model | Multi-Source | Many-to-one | MMS |
|Source Languages|  multiple | one | multiple |
|Target Languages|  one| multiple | multiple |

Multi-Source tries to improve translation by combining of source representation and prediction of different 
translation paths. Many-to-one systems profit from parameter sharing at training time, and MMS can take advantages of both, 
possibly even learn a more general encoding of languages (however, not supported by evidence)
All approaches try to improve their efficiency by training few models than languages pairs or multiple languages.

---

# 7. 
### Exposure Bias and Teacher Forcing
During training, an NMT model typically decodes using only the ground-truth sequence. 
This process, known as **teacher forcing**, ensures that the model learns to predict the next token based on the correct
previous token. However, the model is not exposed to its own predictions during training, which leads to **exposure bias.**
Exposure bias occurs because, at inference time, the model must rely on its own (possibly incorrect) outputs to predict the next token. 
Without exposure during training, the model lacks feedback on how to adjust its parameters to handle these self-generated sequences.


### c) Minimum Risk Training
Minimum Risk Training optimizes directly for sequence-level metrics (e.g., BLEU), improving translation quality by 
focusing on real-world evaluation metrics instead of  traditional likelihood objectives like cross-entropy, which are token-level
based metrics.