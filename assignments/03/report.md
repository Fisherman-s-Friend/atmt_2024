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
(Sennrich and Zhang, 2019) propose a set of strategies and best practices to improve the performance of NMT models in low resource settings.
For this assignment, we will focus on the following strategies:
1. Hyperparameter tuning
2. Byte Pair Encoding (BPE)
which were both shown to improve the performance of NMT models in low resource settings in their paper. They argued for a smaller BPE vocabulary size to 
however, they used the strategies in combination, we will focus on them separately at first and then combine them in a second step.



## Experiment Setup
### Strategy 1
#### Hyperparameter tuning:
In regard to Hyperparameter tuning (Sennrich and Zhang, 2019) highlighted, that best practice differs in low resource settings compared to high resource settings.
They propose to use **smaller batchsizes**, **more aggressive dropout** and **smaller model sizes**, additionally to further strategies. 
Our Idea is to adapt the hyperparameters of the reference model following their proposed strategies.

Their best performing model, trained on 100'000 sentences had the following hyperparameters:

##### Paper model
trained on 100'000 sentences:
* embedding size: 512
* hidden size: 1024
* encoder and decoder depth: 1 
* hidden dropout: 0.5
* embedding dropout: 0.5
* source word dropout: 0.3
* target word dropout: 0.3
* lable smoothing: 0.1
* learning rate: 0.0005
* batch size: 1000 tokens

In comparison, the reference model used in the codebase was trained on 10'000 sentences and had the following hyperparameters:
##### reference model
trained on 10'000: 

* learning rate: 0.0003
* batchsize: 1 
* max tokens: not set

encoder:
* embedding size: 64
* hidden size: 64
* number of layers: 1
* encoder dropout in: 0.25
* encoder dropout out: 0.25

decoder
* embedding size: 64 
* hidden size: 128
* number of layers: 1
* decoder dropout in: 0.25
* decoder dropout out: 0.25
* use attention: True

For the assigment we are confronted with a setting of 10'000 sentences, which is an even smaller dataset, than used in the paper.
We will adapt the hyperparameters of the reference model to the strategies proposed in the paper and compare the performance of the adapted model to the reference model.

Based on the strategies proposed in the paper and the hyperparameter used by the reference model, we  adapt the following hyperparameters:
##### Adapted model
trained on 10'000:

* learning rate: 0.0005 # the paper used this rate, without giving further details
* batchsize: 8 # but it  to increase training speed, even tough the paper suggested to use smaller batchsizes
* max tokens: 1000 # as the paper, however since the reference model used 1 as batchsize (sentence per batch), this might have no influence at all
* bidirectional: True # no change as they suggested to use a bidirectional instead of uni-directional 

encoder:
* embedding size: 64 # we could try to reduce this even more, but we will start with the same size as the reference model, as 64 is already very small
* hidden size: 64 # we could try to reduce this even more, but we will start with the same size as the reference model
* number of layers: 1
* encoder dropout in: 0.5 # as the paper, maybe we could try even more 
* encoder dropout out: 0.5 # as the paper 

decoder
* embedding size: 64 
* hidden size: 128
* number of layers: 1
* decoder dropout in: 0.5 # as the paper
* decoder dropout out: 0.5 # as the paper
* use attention: True # 

##### Model in paper trained on 100'000 used in for the best performing config:
* for both encoder and decoder:
* embedding size: 512
* hidden size: 1024
* encoder and decoder depth: 1 (num layer??)
* hidden dropout: 0.5
* embedding dropout: 0.5
* source word dropout: 0.3
* target word dropout: 0.3
* lable smoothing: 0.1
* learning rate: 0.0005
* batch size: 1000 tokens

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
(venv_new_new) cat assignments/03/model64/translations.p.txt | sacrebleu data/en-fr/raw/test.en
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
 "version": "2.4.3

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

BPE 
with small vocab size: 1000?
(in the paper the used 2000)

## Results

## Discussion

## Conclusion

