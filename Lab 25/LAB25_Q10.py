import re

# Given DNA sequence
dna = "ATCGCGAATTCAC"

# Regular expression for AvaII recognition site
pattern = r"GG(A|T)CC"

# Search for the recognition site
match = re.search(pattern, dna)

if match:
    print("AvaII recognition site found!")
    print("Matching sequence:", match.group())
else:
    print("AvaII recognition site not found.")
