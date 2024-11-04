import sentencepiece as spm

# Define your input files and the output model prefix
input_files = "data/en-fr/raw/train.en,data/en-fr/raw/train.fr"
model_prefix = "bpe_model"
vocab_size = 1000  # Define the size of your vocabulary

# Train the model
spm.SentencePieceTrainer.train(
    input=input_files,
    model_prefix=model_prefix,
    vocab_size=vocab_size,
    model_type="bpe",  # Using BPE model
)

import sentencepiece as spm

# Load the trained SentencePiece model
sp = spm.SentencePieceProcessor(model_file='bpe_model.model')

# Define paths for the input and output files
input_files = ['data/en-fr/raw/train.en', 'data/en-fr/raw/train.fr']
output_files = ['data/en-fr/raw/train.en.bpe', 'data/en-fr/raw/train.fr.bpe']

# Encode each line of each file and save the result
for input_file, output_file in zip(input_files, output_files):
    with open(input_file, 'r', encoding='utf-8') as fin, open(output_file, 'w', encoding='utf-8') as fout:
        for line in fin:
            # Encode each line to BPE tokens
            encoded_line = sp.encode(line.strip(), out_type=str)
            # Join tokens with spaces and write to the output file
            fout.write(' '.join(encoded_line) + '\n')

print("Encoding complete! Encoded files are saved as train.en.bpe and train.fr.bpe.")

