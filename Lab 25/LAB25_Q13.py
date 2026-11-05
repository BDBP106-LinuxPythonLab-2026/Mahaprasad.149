import re

# Given DNA sequence
dna = "ACTNGCATRGCTACGTYACGATSCGAWTCG"

# Regular expression to identify ambiguous bases
pattern = r"[^ATGC]+"

# Split the DNA sequence
result = re.split(pattern, dna)

print("Original DNA sequence:", dna)
print("Split DNA sequence:", result)
