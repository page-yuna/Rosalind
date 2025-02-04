### Complementing a Strand of DNA
# ID: REVC
# Topic: String Algorithm

# Given: A DNA string s of length at most 1000 bp.
# Return: The reverse complement s^c of s.

# Sample Dataset: "AAAACCCGGT"
# Sample Output: "ACCGGGTTTT"

# url: https://rosalind.info/problems/rna/

fpath = "./rosalind_revc.txt"
with open(fpath, 'r') as f:
    seq = f.readline().strip()

complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
rev_c = ''
for i in seq[::-1]:
    rev_c += complement[i]

print(rev_c)
