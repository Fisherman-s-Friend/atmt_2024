your PDF report should be 2-3 pages including figures /
tables and contain the following:
• A detailed description of your experiment setup (Why did you chose these two strategies?
What data did you use? How did you preprocess it? What changes did you make in
the code? Which hyper-parameters did you use for training your models? What training
commands did you use? How did you evaluate your models? ...)

• A suitable presentation and discussion of your results compared to the baseline (table,
visualization, qualitative analysis, ...)

• A final remark on what you learned in this assignment and what you would do differently
next time

adapting hyps: 
![image](https://github.com/user-attachments/assets/06c8d925-b035-4b5e-bd7b-546fb587a5bc)
([Sennrich and Zhang, 2019, p. 4])

most promising: probably easy do modify in code: 
neuron dropout in the paper they used 0.5
reduce batch size :     parser.add_argument('--batch-size', default=1, type=int, help='maximum number of sentences in a batch')
(word) dropout in the paper they used 0.3
model depth 

next time

# Report

## Experiment Setup
### Strategy 1
Hyperparameter tuning:
reference model used: 

@register_model_architecture('lstm', 'lstm')
def base_architecture(args):
    args.encoder_embed_dim = getattr(args, 'encoder_embed_dim', 64) # 2⁶
    args.encoder_embed_path = getattr(args, 'encoder_embed_path', None)
    args.encoder_hidden_size = getattr(args, 'encoder_hidden_size', 64)
    args.encoder_num_layers = getattr(args, 'encoder_num_layers', 1)
    args.encoder_bidirectional = getattr(args, 'encoder_bidirectional', 'True')
    args.encoder_dropout_in = getattr(args, 'encoder_dropout_in', 0.25)
    args.encoder_dropout_out = getattr(args, 'encoder_dropout_out', 0.25)

    args.decoder_embed_dim = getattr(args, 'decoder_embed_dim', 64)
    args.decoder_embed_path = getattr(args, 'decoder_embed_path', None)
    args.decoder_hidden_size = getattr(args, 'decoder_hidden_size', 128) 2⁷
    args.decoder_num_layers = getattr(args, 'decoder_num_layers', 1)
    args.decoder_dropout_in = getattr(args, 'decoder_dropout_in', 0.25)
    args.decoder_dropout_out = getattr(args, 'decoder_dropout_out', 0.25)
    args.decoder_use_attention = getattr(args, 'decoder_use_attention', 'True')
    args.decoder_use_lexical_model = getattr(args, 'decoder_use_lexical_model', 'False')


### Strategy 2

## Results

## Discussion

## Conclusion

