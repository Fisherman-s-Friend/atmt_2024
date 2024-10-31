from tokenizers import Tokenizer
from tokenizers.models import BPE

tokenizer = Tokenizer(BPE())

from tokenizers.pre_tokenizers import Whitespace

tokenizer.pre_tokenizer = Whitespace()
from tokenizers.trainers import BpeTrainer

trainer = BpeTrainer(vocab_size= 1000, special_tokens=["[UNK]"])
Path = "/home/popos/PycharmProjects/atmt_2024_shared/data/en-fr/raw/test.en"
pathfr = "/home/popos/PycharmProjects/atmt_2024_shared/data/en-fr/raw/test.fr"
out_path = "/home/popos/PycharmProjects/atmt_2024_shared/data/en-fr/raw/bpe/tokenizer.json"
out_path ="/home/popos/PycharmProjects/atmt_2024_shared/data/en-fr/bpesmall/tokenizer.json"
tokenizer.train(files=[Path, pathfr, "/home/popos/PycharmProjects/atmt_2024_shared/data/en-fr/raw/train.fr", "/home/popos/PycharmProjects/atmt_2024_shared/data/en-fr/raw/train.en"], trainer=trainer)

output = tokenizer.encode("Hello, y'all! How are you 😁 ?")
print(output.tokens, output.ids)
tokenizer.save(out_path)
# ["Hello", ",", "y", "'", "all", "!", "How", "are", "you", "[UNK]", "?"]