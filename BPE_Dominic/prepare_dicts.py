
from collections import Counter

# Function to create a token frequency dictionary from a file
def create_bpe_dict(file_path, output_dict_path):
    # Count occurrences of each token in the BPE file
    token_counter = Counter()
    with open(file_path, 'r', encoding='utf8') as f:
        for line in f:
            tokens = line.strip().split()
            token_counter.update(tokens)

    # Sort tokens by frequency in descending order
    sorted_tokens = token_counter.most_common()

    # Write to output file in the specified format
    with open(output_dict_path, 'w', encoding='utf8') as f:
        for token, freq in sorted_tokens:
            f.write(f"{token} {freq}\n")

# Create BPE dictionaries for English and French
create_bpe_dict('data/en-fr/bpe_dominic/train.en.bpe', 'data/en-fr/bpe_dominic/dict.en.bpe')
create_bpe_dict('data/en-fr/bpe_dominic/train.fr.bpe', 'data/en-fr/bpe_dominic/dict.fr.bpe')
