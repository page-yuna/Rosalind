### Finding a Motif in DNA
# ID: SUBS
# Topic: String Algorithms

# Given: Two DNA strings s and t (each of length at most 1 kbp).
# Return: All locations of t as a substring of s.

# Sample Dataset:
"""
GATATATGCATATACTT
ATAT
"""
# Sample Output: "2 4 10"

# url: https://rosalind.info/problems/FIB/


def motif_location(seq, motif):
    location = []
    for i in range(len(seq)):
        if seq[i] == motif[0]:
            n = 0
            for j in range(len(motif)):                
                if i+j >= len(seq): break
                if seq[i+j] == motif[j]: n += 1
            if n == len(motif):
                location.append(i+1)
    return location

with open("./rosalind_subs.txt", "r") as f:
     seq, motif = f.read().rstrip().split('\n')

location = motif_location(seq, motif)
for loci in location:
    print(loci, end=' ')
