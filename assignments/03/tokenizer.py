from tokenizers import Tokenizer
from tokenizers.models import BPE

tokenizer = Tokenizer(BPE())

from tokenizers.pre_tokenizers import Whitespace
from tokenizers.processors import ByteLevel

tokenizer.pre_tokenizer = Whitespace()
from tokenizers.trainers import BpeTrainer

trainer = BpeTrainer(vocab_size= 1000, special_tokens=["[UNK]","&apos;"])
Path = "/home/popos/PycharmProjects/atmt_2024_shared/data/en-fr/raw/test.en"
pathfr = "/home/popos/PycharmProjects/atmt_2024_shared/data/en-fr/raw/test.fr"
out_path = "/home/popos/PycharmProjects/atmt_2024_shared/data/en-fr/raw/bpe/tokenizer.json"
out_path ="/home/popos/PycharmProjects/atmt_2024_shared/data/en-fr/bpenew/tokenizer.json"
tokenizer.train(files=[Path, pathfr, "/home/popos/PycharmProjects/atmt_2024_shared/data/en-fr/raw/train.fr", "/home/popos/PycharmProjects/atmt_2024_shared/data/en-fr/raw/train.en"], trainer=trainer)
tokenizer.post_processor = ByteLevel()
output = tokenizer.encode("Hello, y&apos;all! How ar&apos;e you 😁 ? Francaise is my favourite language")
print(output.tokens, output.ids)
tokenizer.save(out_path)
# ["Hello", ",", "y", "'", "all", "!", "How", "are", "you", "[UNK]", "?"]
