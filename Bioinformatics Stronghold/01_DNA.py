### Counting DNA Nucleotides
# ID: DNA
# Topic: String Algorithm

# Given: A DNA string s of length at most 1000 nt.
# Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

# Sample Dataset: "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
# Sample Output: "20 12 17 21"

# url: https://rosalind.info/problems/dna/


def cnt_nu(seq):
    cnt_A, cnt_T, cnt_G, cnt_C = seq.count('A'), seq.count('T'), seq.count('G'), seq.count('C')
    return cnt_A, cnt_C, cnt_G, cnt_T

fpath = "./rosalind_dna.txt"
with open(fpath, 'r') as f:
    seq = f.readline().strip()
    cnt_A, cnt_C, cnt_G, cnt_T = cnt_nu(seq)
    print(cnt_A, cnt_C, cnt_G, cnt_T)
