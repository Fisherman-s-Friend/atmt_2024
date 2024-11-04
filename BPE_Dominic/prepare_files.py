
# Load SentencePiece model
import sentencepiece as spm
sp = spm.SentencePieceProcessor(model_file='bpe_model.model')

# Encode validation file
with open('data/en-fr/raw/test.en', 'r', encoding='utf8') as fin, open('data/en-fr/bpe_dominic/test.en.bpe', 'w', encoding='utf8') as fout:
    for line in fin:
        encoded_line = sp.encode(line.strip(), out_type=str)
        fout.write(' '.join(encoded_line) + '\n')

# Repeat this process for 'valid.fr', 'test.en', 'test.fr', etc.
