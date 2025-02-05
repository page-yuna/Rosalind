### Computing GC Content
# ID: HAMM
# Topic: Alignment

# Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
# Return: The Hamming distance dH(s,t).

# Sample Dataset: 
"""
GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT
"""
# Sample Output: "7"

# url: https://rosalind.info/problems/hamm/


def calc_hamming_distance(fpath):
    with open(fpath, 'r') as f:
        _list = f.read().rstrip().split('\n')
        
    seq1, seq2 = _list[0], _list[1]
    #if len(seq1) != len(seq2):
    #    raise ValueError("두 염기서열의 길이가 다릅니다.")
    
    n_mut = 0
    for i in range(len(seq1)):
        if seq1[i] == seq2[i]: continue
        else: n_mut += 1
    return n_mut


if __name__ == "__main__":
    fpath = "./rosalind_hamm.txt"
    hamm = calc_hamming_distance(fpath)
    print(hamm)
