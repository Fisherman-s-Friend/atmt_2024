from tokenizers import Tokenizer

tokenizer = Tokenizer.from_file("/home/popos/PycharmProjects/atmt_2024_shared/data/en-fr/bpe_new/tokenizer.json")
path = "/assignments/03/models_not_in_report/modelbpe128_new/translations.txt"
with open(path, "r") as file, open("/assignments/03/models_not_in_report/modelbpe128_new/detokenized.txt", "w") as out:
        for line in file:
            ids = [int(i) for i in line.split()]
            out.write(tokenizer.decode(ids))
            out.write("\n")