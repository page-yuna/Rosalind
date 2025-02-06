### Overlap Graphs
# ID: GRPH
# Topic: Graph Algorithms

# Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.
# Return: The adjacency list corresponding to O_3. You may return edges in any order.

# Sample Dataset:
"""
>Rosalind_0498
AAATAAA
>Rosalind_2391
AAATTTT
>Rosalind_2323
TTTTCCC
>Rosalind_0442
AAATCCC
>Rosalind_5013
GGGTGGG
"""
# Sample Output: 
"""
Rosalind_0498 Rosalind_2391
Rosalind_0498 Rosalind_0442
Rosalind_2391 Rosalind_2323
"""

# url: https://rosalind.info/problems/grph/

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

def overlap(seq_dic):
    overlap = []
    for name1 in seq_dic:
        for name2 in seq_dic:
            if name1 != name2:
                if seq_dic[name1][-3:] == seq_dic[name2][:3]:
                    pair = (name1, name2)
                    overlap.append(pair)
                    
    return overlap

fpath = "./rosalind_grph.txt"
with open(fpath, 'r') as f:
    fasta_f = f.read()

    sequences = read_fasta(fasta_f)
    ol_list = overlap(sequences)
    for ol in ol_list:
        print(ol[0], ol[1])
