### Consensus and Profile
# ID: CONS
# Topic: String Algorithms

# Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
# Return: A consensus string and profile matrix for the collection.
#        (If several possible consensus strings exist, then you may return any one of them.)

# Sample Dataset:
"""
>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT
"""
# Sample Output:
"""
ATGCAACT
A: 5 1 0 0 5 5 0 0
C: 0 0 1 4 2 0 6 1
G: 1 1 6 3 0 1 0 0
T: 1 5 0 0 0 1 1 6
"""

# url: https://rosalind.info/problems/cons/


import numpy as np
from collections import Counter

def read_fasta(fasta_str):
    sequences, seq = {}, ''
    for line in fasta_str.strip().split('\n'):
        if line.startswith('>'):
            if seq:
                sequences[name] = seq
                seq = ''
            name = line[1:]
        else: seq += line.strip()
    if seq:
        sequences[name] = seq
    return sequences


def profile(sequences):
    seq_list = list(sequences.values())

    seq_array = np.array([list(seq) for seq in seq_list])
    profiles = [Counter(seq_array[:, i]) for i in range(seq_array.shape[1])]
    nucleotides = ['A', 'C', 'G', 'T']
    profile_matrix = np.array([[counter[nuc] for nuc in nucleotides] for counter in profiles]).T

    max_indices = np.argmax(profile_matrix, axis=0)
    consensus = ''.join([nucleotides[i] for i in max_indices])

    return profile_matrix, consensus


def main(fpath):
    with open(fpath, 'r') as f:
        fasta_f = f.read()

    sequences = read_fasta(fasta_f)
    profile_matrix, consensus = profile(sequences)
    print(consensus)

    for i, nu in enumerate(['A', 'C', 'G', 'T']):
        print(f"{nu}: {' '.join(map(str, profile_matrix[i]))}")


if __name__ == "__main__":
    fpath = "./rosalind_cons.txt"
    main(fpath)
