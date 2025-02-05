### Translating RNA into Protein
# ID: PROT
# Topic: ?

# Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
# Return: The protein string encoded by s.

# Sample Dataset: "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
# Sample Output: "MAMAPRTEINSTRING"

# url: https://rosalind.info/problems/PROT/


from Bio.Seq import Seq

with open("./rosalind_prot.txt", "r") as f:
     rna_seq = Seq(f.read().rstrip())
protein = rna_seq.translate(to_stop=True)
print(protein)
