import os
import subprocess

# Define the beam sizes range
beam_sizes = range(3, 25)

for beam_size in beam_sizes:
    folder = f"assignments/05/beam_{beam_size}"
    
    # Create the folder if it doesn't exist
    # if it exists, continue
    if os.path.exists(folder):
        continue
    os.makedirs(folder)
    
    # Run the translation script
    translate_cmd = [
        "python", "translate_beam.py",
        "--data", "data/en-fr/prepared",
        "--dicts", "data/en-fr/prepared",
        "--checkpoint-path", "assignments/03/baseline/checkpoints/checkpoint_best.pt",
        "--batch-size", "25",
        "--beam-size", str(beam_size),
        "--cuda", "False",
        "--output", f"{folder}/translations.txt"
    ]
    subprocess.run(translate_cmd, check=True)
    
    # Run the postprocessing script
    postprocess_cmd = [
        "bash", "scripts/postprocess.sh",
        f"{folder}/translations.txt",
        f"{folder}/translations.p.txt",
        "en"
    ]
    subprocess.run(postprocess_cmd, check=True)

    # Run the SacreBLEU evaluation
    sacrebleu_cmd = [
        "sacrebleu", "data/en-fr/raw/test.en",
        "-i", f"{folder}/translations.p.txt"
    ]
    print(f"Evaluating BLEU score for beam size {beam_size}...")
    result = subprocess.run(sacrebleu_cmd, capture_output=True, text=True, check=True)
    
    # Save the SacreBLEU output to eval.txt
    eval_file = os.path.join(folder, "eval.txt")
    with open(eval_file, "w") as f:
        f.write(result.stdout)
    print(f"Saved BLEU evaluation to {eval_file}.")
