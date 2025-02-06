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


def read_fasta(fasta_str):
    sequences, seq = {}, ''
    for line in fasta_str.strip().split('\n'):
        if line.startswith('>'):
            if seq:
                sequences[name] = seq
                seq = ''
            name = line.split('>')[1].strip()
        else: seq += line.strip()
    if seq:
        sequences[name] = seq
    return sequences

def profile(sequences):
    profiles = {}
    seq = list(sequences.values())[0]
    for n in range(len(seq)):
        profile = {'A': 0, 'G': 0, 'T': 0, 'C': 0}
        for name in sequences:
            if sequences[name][n] in ('A', 'G', 'T', 'C'):
                profile[sequences[name][n]] += 1

        profiles[n] = profile

    return profiles

def main(fpath):
    with open(fpath, 'r') as f:
        fasta_f = f.read()
    sequences = read_fasta(fasta_f)
    profiles = profile(sequences)

    consensus = ''
    for loci in profiles:
        _dic = profiles[loci]
        con = max(_dic, key=_dic.get)
        consensus += con

    return consensus, profiles

if __name__ == "__main__":
    fpath = "./rosalind_cons.txt"
    consensus, profiles = main(fpath)
    print(consensus)

    for nu in ('A', 'C', 'G', 'T'):
        row_values = [str(profiles[loci][nu]) for loci in profiles]
        print(f"{nu}: {' '.join(row_values)}")
