´´´
python translate_beam.py \
--data data/en-fr/prepared \
--dicts data/en-fr/prepared \
--checkpoint-path assignments/03/baseline/checkpoints/checkpoint_best.pt \
--output assignments/05/baseline/translations.txt \
--batch-size 25 
´´´

´´´
python translate_beam.py --data data/en-fr/prepared --dicts data/en-fr/prepared --checkpoint-path assignments/03/baseline/checkpoints/checkpoint_best.pt --output assignments/05/baseline/translations.txt --batch-size 25 
´´´

´´´
bash scripts/postprocess.sh assignments/05/baseline/translations.txt assignments/05/baseline/translations.p.txt en
´´´

´´´
sacrebleu data/en-fr/raw/test.en -i assignments/05/baseline/translations.p.txt
´´´