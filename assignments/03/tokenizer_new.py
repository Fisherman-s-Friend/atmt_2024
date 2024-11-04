from tokenizers import models, Tokenizer, pre_tokenizers, processors, trainers, decoders, AddedToken

add_token = AddedToken("&apos;", rstrip=True)
tokenizer = Tokenizer(models.BPE(unk_token="[UNK]"))
tokenizer.pre_tokenizer = pre_tokenizers.ByteLevel()
tokenizer.post_processor = processors.ByteLevel()
tokenizer.decoder = decoders.ByteLevel()

trainer = trainers.BpeTrainer(vocab_size= 4000, special_tokens=["[UNK]"])
Path = "/home/popos/PycharmProjects/atmt_2024_shared/data/en-fr/raw/test.en"
pathfr = "/home/popos/PycharmProjects/atmt_2024_shared/data/en-fr/raw/test.fr"
pathpreen ="/home/popos/PycharmProjects/atmt_2024_shared/data/en-fr/preprocessed/test.en"
pathprefr ="/home/popos/PycharmProjects/atmt_2024_shared/data/en-fr/preprocessed/test.fr"
#out_path = "/home/popos/PycharmProjects/atmt_2024_shared/data/en-fr/raw/bpe/tokenizer.json"
out_path ="/home/popos/PycharmProjects/atmt_2024_shared/data/en-fr/bpe/tokenizer.json"
tokenizer.train(files=[Path, pathfr, pathprefr, pathpreen, "/home/popos/PycharmProjects/atmt_2024_shared/data/en-fr/raw/train.fr", "/home/popos/PycharmProjects/atmt_2024_shared/data/en-fr/raw/train.en"], trainer=trainer)

output = tokenizer.encode("je'm appelle Jana found found Hello, y &apos;all! How are you 😁 ? Francaise is my favourite language, I'll get confused")
print(output.tokens, output.ids)
output = tokenizer.decode(output.ids)
print(output)

tokenizer.save(out_path)
