## Training

python train.py \
--data data/en-fr/prepared \
--source-lang fr \
--target-lang en \
--save-dir assignments/03/baselinecheck/checkpoints \
--encoder-embed-dim 64 \
--encoder-hidden-size 64 \
--decoder-embed-dim 64 \
--decoder-hidden-size 128 \
--lr 0.0003 \
--batch-size 8 \
--decoder-dropout-in 0.25 \
--decoder-dropout-out 0.25 \
--encoder-dropout-in 0.25 \
--encoder-dropout-out 0.25 \
--cuda

python train.py \
--data data/en-fr/prepared \
--source-lang fr \
--target-lang en \
--save-dir assignments/03/model32/checkpoints \
--max-token 1000 \
--batch-size 8 \
--encoder-embed-dim 32 \
--encoder-hidden-size 32 \
--decoder-embed-dim 32 \
--decoder-hidden-size 64 \
--lr 0.0005 \
--decoder-dropout-in 0.5 \
--decoder-dropout-out 0.5 \
--encoder-dropout-in 0.5 \
--encoder-dropout-out 0.5 \

python train.py --data data/en-fr/prepared --source-lang fr --target-lang en --save-dir assignments/03/model1/checkpoints --arch lstm --encoder-embed-dim 64 --lr 0.0005 --train-on-tiny


## In-domain Evaluation
´´´
python translate.py \
--data data/en-fr/prepared \
--dicts data/en-fr/prepared \
--checkpoint-path assignments/03/model32/checkpoints/checkpoint_best.pt \
--output assignments/03/baselinecheck/translations.txt \
--cuda \
--batch-size 25
´´´

## postprocess
bash scripts/postprocess.sh \
assignments/03/baselinecheck/translations.txt \
assignments/03/baselinecheck/translations.p.txt en

eval sacrebleu
cat \
assignments/03/modelbpe64/translations.p.txt \
| sacrebleu data/en-fr/raw/test.en


preprocess
python preprocess.py \
    --source-lang fr \
    --target-lang en \
    --train-prefix data/en-fr/preprocessed/train \
    --valid-prefix data/en-fr/preprocessed/valid \
    --test-prefix data/en-fr/preprocessed/test \
    --dest-dir data/en-fr/bpenew\
    --tokenizer bpe \
    --threshold-src 1 \
    --threshold-tgt 1 \
    --num-words-src 1000 \
    --num-words-tgt 1000


python preprocess.py \
    --source-lang $src_lang \
    --target-lang $tgt_lang \
    --dest-dir $prepared \
    --train-prefix $preprocessed/train \
    --valid-prefix $preprocessed/valid \
    --test-prefix $preprocessed/test \
    --tiny-train-prefix $preprocessed/tiny_train \
    --threshold-src 1 \
    --threshold-tgt 1 \
    --num-words-src 4000 \
    --num-words-tgt 4000


    train.py --data /home/user/haller/2022HS/atmt/tests/assignment_03/../../data/en-fr//prepared/ --source-lang fr --target-lang en --save-dir /home/user/haller/2022HS/atmt/tests/assignment_03/baseline/checkpoints --cuda True
INFO: A