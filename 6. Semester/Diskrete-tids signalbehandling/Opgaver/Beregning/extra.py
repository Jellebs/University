from pathlib import Path
import os

# Danish number names from 0 to 99
nummerTilDansk = {
    0: "nul", 1: "en", 2: "to", 3: "tre", 4: "fire", 5: "fem", 6: "seks", 7: "syv", 8: "otte", 9: "ni",
    10: "ti", 11: "elve", 12: "tolv", 13: "tretten", 14: "fjorten", 15: "femten", 16: "seksten", 17: "sytten",
    18: "atten", 19: "nitten", 20: "tyve", 30: "tredive", 40: "fyrre", 50: "halvtreds", 60: "tres",
    70: "halvfjerds", 80: "firs", 90: "halvfems"
}

# Populate 21–99 where necessary
for tiere in [20, 30, 40, 50, 60, 70, 80, 90]:
    for i in range(1, 10):
        nummerTilDansk[tiere + i] = nummerTilDansk[i] + "og" + nummerTilDansk[tiere]

# Start at 100
nummerTilDansk[100] = "ethundrede"

# Add 101–199
for i in range(101, 200):
    under_hundred = i % 100
    navn = nummerTilDansk[under_hundred]
    nummerTilDansk[i] = "ethundredeog" + navn

# Add 200
nummerTilDansk[200] = "tohundrede"

# Convert to hardcoded dictionary format
lines = ["nummerTilDansk = {"]
for k in sorted(nummerTilDansk):
    lines.append(f"    {k}: \"{nummerTilDansk[k]}\",")
lines.append("}")

# Save to file
cwd = os.getcwd()
output_path = Path(cwd + "nummer_til_dansk_0_200.py")
print(cwd + "nummer_til_dansk_0_200.py")
output_path.write_text("\n".join(lines))
output_path.name  # Return file name for user reference