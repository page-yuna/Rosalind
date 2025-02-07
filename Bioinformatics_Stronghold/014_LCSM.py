### Finding a Shared Motif
# ID: LCSM
# Topics: String Algorithms

# Given: Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.
# Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)

# Sample Dataset:
"""
>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA
"""
# Sample Output: "AC"


def sequences_list(fasta_str):
    seq_list, seq = [], ''
    for line in fasta_str.strip().split('\n'):
        if line.startswith('>'):
            if seq:
                seq_list.append(seq)
                seq = ''
        else: seq += line.strip()
    if seq:
        seq_list.append(seq)
    return seq_list

def common_substr(seq_list):
    shortest_seq = min(seq_list, key=len)
    max_len = len(shortest_seq)
    
    common_substr = []
    for l in range(max_len, 0, -1):
        for i in range(max_len - l + 1):
            substr = shortest_seq[i:i+l]
            is_common = True
            for seq in seq_list:
                if substr not in seq:
                    is_common = False
                    break
            if is_common:
                common_substr.append(substr)

    for cs in common_substr:
        longest_cs = max(cs_list, key=len)
      
    return longest_cs

fpath = "./rosalind_lcsm.txt"
with open(fpath, 'r') as f:
    data = f.read()
    seq_list = sequences_list(data)
    longest_cs = common_substr(seq_list)
    print(longest_cs)
