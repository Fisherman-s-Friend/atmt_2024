import os
import pickle

# Load vocabulary dictionary
def load_vocab_dict(dict_path):
    vocab_dict = {}
    max_id = 0
    with open(dict_path, 'r', encoding='utf8') as f:
        for line in f:
            token, index = line.strip().split()
            vocab_dict[token] = int(index)
            max_id = max(max_id, int(index))
    eos_id = max_id + 1  # Use the next available ID as EOS
    return vocab_dict, eos_id

# Load dictionaries and determine EOS IDs
en_dict, en_eos_id = load_vocab_dict('data/en-fr/bpe_dominic_binary/dict.en')
fr_dict, fr_eos_id = load_vocab_dict('data/en-fr/bpe_dominic_binary/dict.fr')

# Convert tokens to IDs and add EOS tokens, saving as binary files
def convert_tokens_to_ids(file_path, vocab_dict, output_path, eos_id):
    data_with_ids = []
    with open(file_path, 'r', encoding='utf8') as f:
        for line in f:
            token_ids = [vocab_dict.get(token, vocab_dict.get("<unk>")) for token in line.strip().split()]
            token_ids.append(eos_id)  # Append EOS token ID
            data_with_ids.append(token_ids)
    
    with open(output_path, 'wb') as f:
        pickle.dump(data_with_ids, f)

# Directory paths
input_dir = 'data/en-fr/bpe_dominic'
output_dir = 'data/en-fr/bpe_dominic_binary'
os.makedirs(output_dir, exist_ok=True)

# Process each file in the directory
for filename in os.listdir(input_dir):
    if filename not in ['dict.en', 'dict.fr']:
        if filename.endswith('.en'):
            vocab_dict = en_dict
            eos_id = en_eos_id
        elif filename.endswith('.fr'):
            vocab_dict = fr_dict
            eos_id = fr_eos_id
        else:
            continue  # Skip non-.en and .fr files

        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, f'{filename}')
        convert_tokens_to_ids(input_path, vocab_dict, output_path, eos_id)

print("Conversion completed. Binary files with EOS IDs are saved in", output_dir)
