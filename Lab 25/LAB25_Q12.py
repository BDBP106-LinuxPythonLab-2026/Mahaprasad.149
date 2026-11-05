import re

# Given DNA sequence
dna = "ATCGCGYAATTCAC"

# Check for ambiguous bases
pattern = r"[^ATGC]"

match = re.search(pattern, dna)

if match:
    print("Ambiguous bases found!")

    # Print non-ambiguous bases
    non_ambiguous = re.sub(pattern, "", dna)

    print("Non-ambiguous DNA sequence:", non_ambiguous)

else:
    print("No ambiguous bases found.")
    print("DNA sequence:", dna)