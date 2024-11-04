INFO: Commencing training!
INFO: COMMAND: train.py --data data/en-fr/prepared --source-lang fr --target-lang en --save-dir assignments/03/baselinecheck/checkpoints --encoder-embed-dim 64 --encoder-hidden-size 64 --decoder-embed-dim 64 --decoder-hidden-size 128 --lr 0.0003 --batch-size 8 --decoder-dropout-in 0.25 --decoder-dropout-out 0.25 --encoder-dropout-in 0.25 --encoder-dropout-out 0.25 --cuda
INFO: Arguments: {'cuda': True, 'data': 'data/en-fr/prepared', 'source_lang': 'fr', 'target_lang': 'en', 'max_tokens': None, 'batch_size': 8, 'train_on_tiny': False, 'arch': 'lstm', 'max_epoch': 10000, 'clip_norm': 4.0, 'lr': 0.0003, 'patience': 3, 'log_file': None, 'save_dir': 'assignments/03/baselinecheck/checkpoints', 'restore_file': 'checkpoint_last.pt', 'save_interval': 1, 'no_save': False, 'epoch_checkpoints': False, 'encoder_embed_dim': 64, 'encoder_hidden_size': 64, 'decoder_embed_dim': 64, 'decoder_hidden_size': 128, 'decoder_dropout_in': 0.25, 'decoder_dropout_out': 0.25, 'encoder_dropout_in': '0.25', 'encoder_dropout_out': '0.25', 'encoder_embed_path': None, 'encoder_num_layers': 1, 'encoder_bidirectional': 'True', 'decoder_embed_path': None, 'decoder_num_layers': 1, 'decoder_use_attention': 'True', 'decoder_use_lexical_model': 'False', 'device_id': 0}
INFO: Loaded a source dictionary (fr) with 4000 words
INFO: Loaded a target dictionary (en) with 4000 words
INFO: Built a model with 1308576 parameters
INFO: Epoch 000: loss 5.006 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 12.16 | clip 0.9768                                                                                                                             
INFO: Epoch 000: valid_loss 5.16 | num_tokens 9.14 | batch_size 500 | valid_perplexity 174
INFO: Epoch 001: loss 4.407 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 11.08 | clip 1                                                                                                                                  
INFO: Epoch 001: valid_loss 4.85 | num_tokens 9.14 | batch_size 500 | valid_perplexity 127
INFO: Epoch 002: loss 4.158 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 11.31 | clip 1                                                                                                                                  
INFO: Epoch 002: valid_loss 4.52 | num_tokens 9.14 | batch_size 500 | valid_perplexity 92.1
INFO: Epoch 003: loss 3.966 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 11.75 | clip 1                                                                                                                                  
INFO: Epoch 003: valid_loss 4.36 | num_tokens 9.14 | batch_size 500 | valid_perplexity 77.9
INFO: Epoch 004: loss 3.802 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 12.45 | clip 1                                                                                                                                  
INFO: Epoch 004: valid_loss 4.24 | num_tokens 9.14 | batch_size 500 | valid_perplexity 69.7
INFO: Epoch 005: loss 3.665 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 13 | clip 1                                                                                                                                     
INFO: Epoch 005: valid_loss 4.09 | num_tokens 9.14 | batch_size 500 | valid_perplexity 59.6
INFO: Epoch 006: loss 3.532 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 13.69 | clip 1                                                                                                                                  
INFO: Epoch 006: valid_loss 3.99 | num_tokens 9.14 | batch_size 500 | valid_perplexity 53.9
INFO: Epoch 007: loss 3.417 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 13.89 | clip 1                                                                                                                                  
INFO: Epoch 007: valid_loss 3.91 | num_tokens 9.14 | batch_size 500 | valid_perplexity 50.1
INFO: Epoch 008: loss 3.314 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 14.34 | clip 1                                                                                                                                  
INFO: Epoch 008: valid_loss 3.78 | num_tokens 9.14 | batch_size 500 | valid_perplexity 43.9
INFO: Epoch 009: loss 3.218 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 14.9 | clip 1                                                                                                                                   
INFO: Epoch 009: valid_loss 3.69 | num_tokens 9.14 | batch_size 500 | valid_perplexity 40.2
INFO: Epoch 010: loss 3.132 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 15.34 | clip 1                                                                                                                                  
INFO: Epoch 010: valid_loss 3.64 | num_tokens 9.14 | batch_size 500 | valid_perplexity 38.1
INFO: Epoch 011: loss 3.057 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 15.89 | clip 1                                                                                                                                  
INFO: Epoch 011: valid_loss 3.51 | num_tokens 9.14 | batch_size 500 | valid_perplexity 33.3
INFO: Epoch 012: loss 2.984 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 16.19 | clip 1                                                                                                                                  
INFO: Epoch 012: valid_loss 3.48 | num_tokens 9.14 | batch_size 500 | valid_perplexity 32.5
INFO: Epoch 013: loss 2.923 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 16.5 | clip 1                                                                                                                                   
INFO: Epoch 013: valid_loss 3.37 | num_tokens 9.14 | batch_size 500 | valid_perplexity 29.1
INFO: Epoch 014: loss 2.848 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 16.86 | clip 1                                                                                                                                  
INFO: Epoch 014: valid_loss 3.32 | num_tokens 9.14 | batch_size 500 | valid_perplexity 27.8
INFO: Epoch 015: loss 2.794 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 17.01 | clip 1                                                                                                                                  
INFO: Epoch 015: valid_loss 3.26 | num_tokens 9.14 | batch_size 500 | valid_perplexity 26.1
INFO: Epoch 016: loss 2.729 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 17.51 | clip 1                                                                                                                                  
INFO: Epoch 016: valid_loss 3.23 | num_tokens 9.14 | batch_size 500 | valid_perplexity 25.3
INFO: Epoch 017: loss 2.678 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 17.74 | clip 1                                                                                                                                  
INFO: Epoch 017: valid_loss 3.19 | num_tokens 9.14 | batch_size 500 | valid_perplexity 24.2
INFO: Epoch 018: loss 2.624 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 18.21 | clip 1                                                                                                                                  
INFO: Epoch 018: valid_loss 3.13 | num_tokens 9.14 | batch_size 500 | valid_perplexity 22.9
INFO: Epoch 019: loss 2.578 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 18.48 | clip 1                                                                                                                                  
INFO: Epoch 019: valid_loss 3.1 | num_tokens 9.14 | batch_size 500 | valid_perplexity 22.3
INFO: Epoch 020: loss 2.529 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 18.79 | clip 1                                                                                                                                  
INFO: Epoch 020: valid_loss 3.05 | num_tokens 9.14 | batch_size 500 | valid_perplexity 21.1
INFO: Epoch 021: loss 2.48 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 19.08 | clip 1                                                                                                                                   
INFO: Epoch 021: valid_loss 3.04 | num_tokens 9.14 | batch_size 500 | valid_perplexity 20.9
INFO: Epoch 022: loss 2.435 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 19.4 | clip 1                                                                                                                                   
INFO: Epoch 022: valid_loss 2.94 | num_tokens 9.14 | batch_size 500 | valid_perplexity 18.9
INFO: Epoch 023: loss 2.39 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 19.62 | clip 1                                                                                                                                   
INFO: Epoch 023: valid_loss 2.93 | num_tokens 9.14 | batch_size 500 | valid_perplexity 18.7
INFO: Epoch 024: loss 2.349 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 19.76 | clip 1                                                                                                                                  
INFO: Epoch 024: valid_loss 2.88 | num_tokens 9.14 | batch_size 500 | valid_perplexity 17.8
INFO: Epoch 025: loss 2.307 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 20.03 | clip 1                                                                                                                                  
INFO: Epoch 025: valid_loss 2.88 | num_tokens 9.14 | batch_size 500 | valid_perplexity 17.9
INFO: Epoch 026: loss 2.267 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 20.25 | clip 1                                                                                                                                  
INFO: Epoch 026: valid_loss 2.83 | num_tokens 9.14 | batch_size 500 | valid_perplexity 16.9
INFO: Epoch 027: loss 2.232 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 20.63 | clip 1                                                                                                                                  
INFO: Epoch 027: valid_loss 2.81 | num_tokens 9.14 | batch_size 500 | valid_perplexity 16.6
INFO: Epoch 028: loss 2.2 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 20.65 | clip 1                                                                                                                                    
INFO: Epoch 028: valid_loss 2.77 | num_tokens 9.14 | batch_size 500 | valid_perplexity 15.9
INFO: Epoch 029: loss 2.164 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 20.95 | clip 1                                                                                                                                  
INFO: Epoch 029: valid_loss 2.73 | num_tokens 9.14 | batch_size 500 | valid_perplexity 15.3
INFO: Epoch 030: loss 2.128 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 21 | clip 1                                                                                                                                     
INFO: Epoch 030: valid_loss 2.72 | num_tokens 9.14 | batch_size 500 | valid_perplexity 15.1
INFO: Epoch 031: loss 2.092 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 21.15 | clip 1                                                                                                                                  
INFO: Epoch 031: valid_loss 2.7 | num_tokens 9.14 | batch_size 500 | valid_perplexity 14.9
INFO: Epoch 032: loss 2.068 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 21.29 | clip 1                                                                                                                                  
INFO: Epoch 032: valid_loss 2.68 | num_tokens 9.14 | batch_size 500 | valid_perplexity 14.5
INFO: Epoch 033: loss 2.039 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 21.79 | clip 1                                                                                                                                  
INFO: Epoch 033: valid_loss 2.65 | num_tokens 9.14 | batch_size 500 | valid_perplexity 14.1
INFO: Epoch 034: loss 2.01 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 21.49 | clip 1                                                                                                                                   
INFO: Epoch 034: valid_loss 2.63 | num_tokens 9.14 | batch_size 500 | valid_perplexity 13.9
INFO: Epoch 035: loss 1.982 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 21.88 | clip 1                                                                                                                                  
INFO: Epoch 035: valid_loss 2.6 | num_tokens 9.14 | batch_size 500 | valid_perplexity 13.5
INFO: Epoch 036: loss 1.955 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 21.9 | clip 1                                                                                                                                   
INFO: Epoch 036: valid_loss 2.6 | num_tokens 9.14 | batch_size 500 | valid_perplexity 13.5
INFO: Epoch 037: loss 1.927 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 21.89 | clip 1                                                                                                                                  
INFO: Epoch 037: valid_loss 2.6 | num_tokens 9.14 | batch_size 500 | valid_perplexity 13.5
INFO: Epoch 038: loss 1.902 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 22.17 | clip 1                                                                                                                                  
INFO: Epoch 038: valid_loss 2.55 | num_tokens 9.14 | batch_size 500 | valid_perplexity 12.8
INFO: Epoch 039: loss 1.875 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 22.28 | clip 1                                                                                                                                  
INFO: Epoch 039: valid_loss 2.54 | num_tokens 9.14 | batch_size 500 | valid_perplexity 12.7
INFO: Epoch 040: loss 1.848 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 22.44 | clip 1                                                                                                                                  
INFO: Epoch 040: valid_loss 2.55 | num_tokens 9.14 | batch_size 500 | valid_perplexity 12.8
INFO: Epoch 041: loss 1.823 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 22.67 | clip 1                                                                                                                                  
INFO: Epoch 041: valid_loss 2.52 | num_tokens 9.14 | batch_size 500 | valid_perplexity 12.5
INFO: Epoch 042: loss 1.803 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 22.61 | clip 1                                                                                                                                  
INFO: Epoch 042: valid_loss 2.5 | num_tokens 9.14 | batch_size 500 | valid_perplexity 12.2
INFO: Epoch 043: loss 1.78 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 22.6 | clip 1                                                                                                                                    
INFO: Epoch 043: valid_loss 2.5 | num_tokens 9.14 | batch_size 500 | valid_perplexity 12.2
INFO: Epoch 044: loss 1.76 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 22.73 | clip 1                                                                                                                                   
INFO: Epoch 044: valid_loss 2.48 | num_tokens 9.14 | batch_size 500 | valid_perplexity 11.9
INFO: Epoch 045: loss 1.742 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 22.76 | clip 1                                                                                                                                  
INFO: Epoch 045: valid_loss 2.5 | num_tokens 9.14 | batch_size 500 | valid_perplexity 12.1
INFO: Epoch 046: loss 1.722 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 23.24 | clip 1                                                                                                                                  
INFO: Epoch 046: valid_loss 2.48 | num_tokens 9.14 | batch_size 500 | valid_perplexity 11.9
INFO: Epoch 047: loss 1.699 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 23.08 | clip 1                                                                                                                                  
INFO: Epoch 047: valid_loss 2.47 | num_tokens 9.14 | batch_size 500 | valid_perplexity 11.8
INFO: Epoch 048: loss 1.686 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 23.02 | clip 1                                                                                                                                  
INFO: Epoch 048: valid_loss 2.46 | num_tokens 9.14 | batch_size 500 | valid_perplexity 11.7
INFO: Epoch 049: loss 1.665 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 23.08 | clip 1                                                                                                                                  
INFO: Epoch 049: valid_loss 2.46 | num_tokens 9.14 | batch_size 500 | valid_perplexity 11.7
INFO: Epoch 050: loss 1.646 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 23.23 | clip 1                                                                                                                                  
INFO: Epoch 050: valid_loss 2.45 | num_tokens 9.14 | batch_size 500 | valid_perplexity 11.6
INFO: Epoch 051: loss 1.63 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 23.38 | clip 1                                                                                                                                   
INFO: Epoch 051: valid_loss 2.43 | num_tokens 9.14 | batch_size 500 | valid_perplexity 11.4
INFO: Epoch 052: loss 1.615 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 23.48 | clip 1                                                                                                                                  
INFO: Epoch 052: valid_loss 2.42 | num_tokens 9.14 | batch_size 500 | valid_perplexity 11.3
INFO: Epoch 053: loss 1.595 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 23.49 | clip 1                                                                                                                                  
INFO: Epoch 053: valid_loss 2.42 | num_tokens 9.14 | batch_size 500 | valid_perplexity 11.3
INFO: Epoch 054: loss 1.585 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 23.65 | clip 1                                                                                                                                  
INFO: Epoch 054: valid_loss 2.41 | num_tokens 9.14 | batch_size 500 | valid_perplexity 11.2
INFO: Epoch 055: loss 1.564 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 23.55 | clip 1                                                                                                                                  
INFO: Epoch 055: valid_loss 2.45 | num_tokens 9.14 | batch_size 500 | valid_perplexity 11.6
INFO: Epoch 056: loss 1.55 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 23.68 | clip 1                                                                                                                                   
INFO: Epoch 056: valid_loss 2.44 | num_tokens 9.14 | batch_size 500 | valid_perplexity 11.5
INFO: Epoch 057: loss 1.534 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 23.7 | clip 1                                                                                                                                   
INFO: Epoch 057: valid_loss 2.4 | num_tokens 9.14 | batch_size 500 | valid_perplexity 11
INFO: Epoch 058: loss 1.519 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 23.69 | clip 1                                                                                                                                  
INFO: Epoch 058: valid_loss 2.4 | num_tokens 9.14 | batch_size 500 | valid_perplexity 11
INFO: Epoch 059: loss 1.503 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 23.8 | clip 1                                                                                                                                   
INFO: Epoch 059: valid_loss 2.38 | num_tokens 9.14 | batch_size 500 | valid_perplexity 10.8
INFO: Epoch 060: loss 1.493 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 23.9 | clip 1                                                                                                                                   
INFO: Epoch 060: valid_loss 2.37 | num_tokens 9.14 | batch_size 500 | valid_perplexity 10.7
INFO: Epoch 061: loss 1.475 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 23.58 | clip 1                                                                                                                                  
INFO: Epoch 061: valid_loss 2.38 | num_tokens 9.14 | batch_size 500 | valid_perplexity 10.9
INFO: Epoch 062: loss 1.466 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 23.8 | clip 1                                                                                                                                   
INFO: Epoch 062: valid_loss 2.37 | num_tokens 9.14 | batch_size 500 | valid_perplexity 10.7
INFO: Epoch 063: loss 1.449 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 23.92 | clip 1                                                                                                                                  
INFO: Epoch 063: valid_loss 2.37 | num_tokens 9.14 | batch_size 500 | valid_perplexity 10.7
INFO: Epoch 064: loss 1.438 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 24.2 | clip 1                                                                                                                                   
INFO: Epoch 064: valid_loss 2.35 | num_tokens 9.14 | batch_size 500 | valid_perplexity 10.5
INFO: Epoch 065: loss 1.427 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 23.92 | clip 1                                                                                                                                  
INFO: Epoch 065: valid_loss 2.36 | num_tokens 9.14 | batch_size 500 | valid_perplexity 10.6
INFO: Epoch 066: loss 1.413 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 23.98 | clip 1                                                                                                                                  
INFO: Epoch 066: valid_loss 2.35 | num_tokens 9.14 | batch_size 500 | valid_perplexity 10.5
INFO: Epoch 067: loss 1.403 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 24.28 | clip 1                                                                                                                                  
INFO: Epoch 067: valid_loss 2.34 | num_tokens 9.14 | batch_size 500 | valid_perplexity 10.4
INFO: Epoch 068: loss 1.387 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 24.03 | clip 1                                                                                                                                  
INFO: Epoch 068: valid_loss 2.35 | num_tokens 9.14 | batch_size 500 | valid_perplexity 10.5
INFO: Epoch 069: loss 1.383 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 24.09 | clip 1                                                                                                                                  
INFO: Epoch 069: valid_loss 2.36 | num_tokens 9.14 | batch_size 500 | valid_perplexity 10.6
INFO: Epoch 070: loss 1.37 | lr 0.0003 | num_tokens 9.1 | batch_size 8 | grad_norm 24.17 | clip 1                                                                                                                                   
INFO: Epoch 070: valid_loss 2.35 | num_tokens 9.14 | batch_size 500 | valid_perplexity 10.5


assignments/03/baselinecheck/translations.p.txt \
| sacrebleu data/en-fr/raw/test.en
{
 "name": "BLEU",
 "score": 17.7,
 "signature": "nrefs:1|case:mixed|eff:no|tok:13a|smooth:exp|version:2.4.3",
 "verbose_score": "48.0/23.2/12.6/7.0 (BP = 1.000 ratio = 1.190 hyp_len = 4631 ref_len = 3892)",
 "nrefs": "1",
 "case": "mixed",
 "eff": "no",
 "tok": "13a",
 "smooth": "exp",
 "version": "2.4.3"
}
