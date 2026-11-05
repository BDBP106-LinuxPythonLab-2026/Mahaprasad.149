import re

# Given DNA sequence
dna = "ATCGCGAATTCAC"

# Regular expression pattern for BisI
pattern = r"GC[ATGC]GC"

# Search for the restriction site
match = re.search(pattern, dna)

if match:
    print("BisI restriction site found!")
    print("Matching sequence:", match.group())
else:
    print("BisI restriction site not found.")
