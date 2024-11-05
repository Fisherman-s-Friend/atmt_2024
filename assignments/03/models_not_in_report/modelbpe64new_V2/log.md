cat assignments/03/modelbpe64_new/translations.p.txt | sacrebleu data/en-fr/raw/test.en
{
 "name": "BLEU",
 "score": 16.2,
 "signature": "nrefs:1|case:mixed|eff:no|tok:13a|smooth:exp|version:2.4.3",
 "verbose_score": "46.3/21.4/11.6/6.0 (BP = 1.000 ratio = 1.169 hyp_len = 4550 ref_len = 3892)",
 "nrefs": "1",
 "case": "mixed",
 "eff": "no",
 "tok": "13a",
 "smooth": "exp",
 "version": "2.4.3"
}

 train.py --data data/en-fr/bpe --source-lang fr --target-lang en --save-dir assignments/03/modelbpe64_new/checkpoints --encoder-embed-dim 64 --encoder-hidden-size 64 --decoder-embed-dim 64 --decoder-hidden-size 128 --lr 0.0003 --max-token 1000 --batch-size 8 --decoder-dropout-in 0.25 --decoder-dropout-out 0.25 --encoder-dropout-in 0.25 --encoder-dropout-out 0.25 --cuda
INFO: Arguments: {'cuda': True, 'data': 'data/en-fr/bpe', 'source_lang': 'fr', 'target_lang': 'en', 'max_tokens': 1000, 'batch_size': 8, 'train_on_tiny': False, 'arch': 'lstm', 'max_epoch': 10000, 'clip_norm': 4.0, 'lr': 0.0003, 'patience': 3, 'log_file': None, 'save_dir': 'assignments/03/modelbpe64_new/checkpoints', 'restore_file': 'checkpoint_last.pt', 'save_interval': 1, 'no_save': False, 'epoch_checkpoints': False, 'encoder_embed_dim': 64, 'encoder_hidden_size': 64, 'decoder_embed_dim': 64, 'decoder_hidden_size': 128, 'decoder_dropout_in': 0.25, 'decoder_dropout_out': 0.25, 'encoder_dropout_in': '0.25', 'encoder_dropout_out': '0.25', 'encoder_embed_path': None, 'encoder_num_layers': 1, 'encoder_bidirectional': 'True', 'decoder_embed_path': None, 'decoder_num_layers': 1, 'decoder_use_attention': 'True', 'decoder_use_lexical_model': 'False', 'device_id': 0}
INFO: Loaded a source dictionary (fr) with 2000 words
INFO: Loaded a target dictionary (en) with 2000 words
INFO: Built a model with 794576 parameters
