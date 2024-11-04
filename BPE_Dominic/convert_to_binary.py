
import os
import pickle

# Directory containing BPE files
input_dir = 'data/en-fr/bpe_dominic_binary'
output_dir = 'data/en-fr/bpe_dominic_binary'

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Iterate over each file in the input directory
for filename in os.listdir(input_dir):
    if filename not in ['dict.en', 'dict.fr']:
        # Read the content of the BPE file
        with open(os.path.join(input_dir, filename), 'r', encoding='utf8') as f:
            lines = [line.strip().split() for line in f]  # Tokenized lines as lists of tokens

        # Save to binary format
        with open(os.path.join(output_dir, f'{filename}'), 'wb') as f:
            pickle.dump(lines, f)

print("All eligible files have been converted to binary format and saved in", output_dir)
