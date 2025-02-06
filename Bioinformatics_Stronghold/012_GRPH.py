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

def ...

with open(fpath, 'r') as f:
    fasta_f = f.read()

sequences = read_fasta(fasta_f)
