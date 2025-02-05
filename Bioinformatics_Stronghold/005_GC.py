### Computing GC Content
# ID: GC
# Topic: String Algorithm

# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
# Return: The ID of the string having the highest GC-content, followed by the GC-content of that string.
#         Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated;
#         please see the note on absolute error below.

# Sample Dataset:
""" 
>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT
"""
# Sample Output: 
"""
Rosalind_0808
60.919540
"""

# url: https://rosalind.info/problems/gc/


def read_fasta(fasta_str):
    sequences = {}
    seq = ''
    for line in fasta_str.strip().split('\n'):
        if line.startswith('>'):
            if seq:
                sequences[chromosome] = seq
                seq = ''
            chromosome = line[1:]
        else: seq += line.strip()
    if seq:
        sequences[chromosome] = seq
    return sequences

def process_fasta_file(fpath):
    with open(fpath, 'r') as f:
        fasta_f = f.read()
    fasta = read_fasta(fasta_f)
    gc_contents = {}
    for name in fasta:
        seq = fasta[name]
        gc_contents[name] = (seq.count('G') + seq.count('C')) / len(seq) * 100
    max_gc_name = max(gc_contents, key=gc_contents.get)
    return max_gc_name, gc_contents[max_gc_name]

if __name__ == "__main__":
    fpath = "./rosalind_gc.txt"
    max_gc_name, max_gc_content = process_fasta_file(fpath)
    print(max_gc_name)
    print(f"{max_gc_content:.6f}")
