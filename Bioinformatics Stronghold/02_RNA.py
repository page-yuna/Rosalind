### Transcribing DNA into RNA
# ID: RNA
# Topic: String Algorithm

# Given: A DNA string t having length at most 1000 nt.
# Return: The transcribed RNA string of t.

# Sample Dataset: "GATGGAACTTGACTACGTAAATT"
# Sample Output: "GAUGGAACUUGACUACGUAAAUU"

# url: https://rosalind.info/problems/rna/


fpath = "./rosalind_rna.txt"
with open(fpath, 'r') as f:
    seq = f.readline().strip()
    rna_seq = seq.replace('T', 'U')
    print(rna_seq)
