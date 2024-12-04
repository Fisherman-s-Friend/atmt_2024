import os
import json
import matplotlib.pyplot as plt

base_folder = "assignments/05"
bleu_scores = {}

# Load BLEU scores and brevity penalties
for folder in os.listdir(base_folder):
    # Skip non-folders
    if not os.path.isdir(os.path.join(base_folder, folder)):
        continue

    eval_file = os.path.join(base_folder, folder, "eval.txt")
    try:
        with open(eval_file) as f:
            data = json.load(f)
            bleu_score = data["score"]
            # Extract brevity penalty from verbose_score
            brevity_penalty = float(data["verbose_score"].split("BP = ")[1].split()[0])
            length = data["verbose_score"]
    except FileNotFoundError:
        continue

    folder_adjusted = (
        folder
        if folder == "baseline" or len(folder.split("_")[1]) == 2
        else folder.split("_")[0] + "_0" + folder.split("_")[1]
    )
    bleu_scores[folder_adjusted] = (bleu_score, brevity_penalty, length)

# Sort the dictionary by key
bleu_scores = dict(sorted(bleu_scores.items()))
beam_sizes = bleu_scores.keys()
bleu_values = [val[0] for val in bleu_scores.values()]
bp_values = [val[1] for val in bleu_scores.values()]
len_values = [val[2] for val in bleu_scores.values()]
for l in len_values:
    print(l)

# Plot BLEU scores
fig, ax1 = plt.subplots(figsize=(12, 6))
bars_bleu = ax1.bar(
    beam_sizes, bleu_values, color="lightgreen", label="BLEU Score", alpha=0.8
)
ax1.set_xlabel("Beam Size")
ax1.set_ylabel("BLEU Score", fontsize=14, color="lightgreen")
ax1.tick_params(axis="y")
ax1.set_title("BLEU Scores and Brevity Penalties for Different Beam Sizes")
plt.xticks(rotation=45)

# Add BLEU score values above the bars
for bar, bleu_score in zip(bars_bleu, bleu_values):
    height = bar.get_height()
    ax1.text(
        bar.get_x() + bar.get_width() / 2,
        height + 0.3,
        f"{bleu_score:.2f}",
        ha="center",
        va="bottom",
        fontsize=9,
    )

# Plot brevity penalties on the secondary y-axis
ax2 = ax1.twinx()
bars_bp = ax2.bar(
    beam_sizes, bp_values, color="orange", width=0.4, label="Brevity Penalty", alpha=0.6
)
ax2.set_ylabel("Brevity Penalty (BP)", fontsize=14, color="orange")
ax2.tick_params(axis="y")

# Set the right y-axis limit to 1.5
ax2.set_ylim(0, 1.5)

# Add BP values above the BP bars
for bar, bp in zip(bars_bp, bp_values):
    height = bar.get_height()
    ax2.text(
        bar.get_x() + bar.get_width() / 2,
        height + 0.02,
        f"{bp:.2f}",
        ha="center",
        va="bottom",
        fontsize=8,
    )

# Adjust layout and show the plot
fig.tight_layout()
#plt.show()
