### Mendel's First Law
# ID: IPRB
# Topic: Heredity, Probability

# Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
# Return: The Hamming distance dH(s,t).

# Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms
#        : k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

# Return: The probability that two randomly selected mating organisms will produce
#         an individual possessing a dominant allele (and thus displaying the dominant phenotype).
#         Assume that any two organisms can mate.

# Sample Dataset: "2 2 2"
# Sample Output: "0.78333"

# url: https://rosalind.info/problems/iprb/


def calc_dominant_prob(k, m, n):
    total = k + m + n
    total_pairs = total * (total - 1)
    
    prob_AA_AA = (k * (k - 1)) * 1
    prob_AA_Aa = (k * m + m * k) * 1
    prob_AA_aa = (k * n + n * k) * 1
    prob_Aa_Aa = (m * (m - 1)) * 0.75
    prob_Aa_aa = (m * n + n * m) * 0.5
    prob_aa_aa = (n * (n - 1)) * 0
    
    total_dominant = (prob_AA_AA + prob_AA_Aa + prob_AA_aa + prob_Aa_Aa + prob_Aa_aa + prob_aa_aa)

    prob = total_dominant / total_pairs
    return round(prob, 5)

with open("./rosalind_iprb.txt", "r") as f:
    k, m, n = map(int, f.readline().split())

prob = calc_dominant_prob(k, m, n)
print(f"{prob:.5f}")
