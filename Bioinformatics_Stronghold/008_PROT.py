### Translating RNA into Protein
# ID: PROT
# Topic: ?

# Given: 
# Return: 

# Sample Dataset:
# Sample Output: 

# url: https://rosalind.info/problems/PROT/


from Bio.Seq import Seq

with open("./rosalind_prot.txt", "r") as f:
     rna_seq = Seq(f.read().rstrip())
protein = rna_seq.translate(to_stop=True)
print(protein)
