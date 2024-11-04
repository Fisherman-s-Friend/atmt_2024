import pickle

with open('data/en-fr/bpenew/train.fr', 'rb') as f:
    sample_data = pickle.load(f)

with open('sample_data_output.txt', 'w', encoding='utf-8') as out_file:
    for item in sample_data:  # Adjust to print more if needed
        out_file.write(str(item) + '\n')

print("Sample data has been written to sample_data_output.txt")
