{
 "name": "BLEU",
 "score": 0.6,
 "signature": "nrefs:1|case:mixed|eff:no|tok:13a|smooth:exp|version:2.4.3",
 "verbose_score": "17.0/1.4/0.2/0.0 (BP = 1.000 ratio = 1.695 hyp_len = 6598 ref_len = 3892)",
 "nrefs": "1",
 "case": "mixed",
 "eff": "no",
 "tok": "13a",
 "smooth": "exp",
 "version": "2.4.3"
}
 train.py --data data/en-fr/prepared --source-lang fr --target-lang en --save-dir assignments/03/model32/checkpoints --max-token 1000 --batch-size 8 --encoder-embed-dim 32 --encoder-hidden-size 32 --decoder-embed-dim 32 --decoder-hidden-size 64 --lr 0.0005 --decoder-dropout-in 0.5 --decoder-dropout-out 0.5 --encoder-dropout-in 0.5 --encoder-dropout-out 0.5 --cuda
INFO: Arguments: {'cuda': True, 'data': 'data/en-fr/prepared', 'source_lang': 'fr', 'target_lang': 'en', 'max_tokens': 1000, 'batch_size': 1, 'train_on_tiny': False, 'arch': 'lstm', 'max_epoch': 10000, 'clip_norm': 4.0, 'lr': 0.0005, 'patience': 3, 'log_file': None, 'save_dir': 'assignments/03/model32/checkpoints', 'restore_file': 'checkpoint_last.pt', 'save_interval': 1, 'no_save': False, 'epoch_checkpoints': False, 'encoder_embed_dim': 32, 'encoder_hidden_size': 32, 'decoder_embed_dim': 32, 'decoder_hidden_size': 64, 'decoder_dropout_in': 0.5, 'decoder_dropout_out': 0.5, 'encoder_dropout_in': '0.5', 'encoder_dropout_out': '0.5', 'encoder_embed_path': None, 'encoder_num_layers': 1, 'encoder_bidirectional': 'True', 'decoder_embed_path': None, 'decoder_num_layers': 1, 'decoder_use_attention': 'True', 'decoder_use_lexical_model': 'False', 'device_id': 0}
INFO: Loaded a source dictionary (fr) with 4000 words
INFO: Loaded a target dictionary (en) with 4000 words
