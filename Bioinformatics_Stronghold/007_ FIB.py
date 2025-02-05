### Rabbits and Recurrence Relations
# ID: FIB
# Topic: Combinatorics, Dynamic Programming

# Given: Positive integers n≤40 and k≤5.
# Return: The total number of rabbit pairs that will be present after n months,
#         if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces
#         a litter of k rabbit pairs (instead of only 1 pair).

# Sample Dataset: "5 3"
# Sample Output: "19"

# url: https://rosalind.info/problems/FIB/


def rabbit_pairs(n, k):
    # Base cases
    if n == 1 or n == 2: return 1

    rabbits = [0] * (n + 1)
    rabbits[1], rabbits[2] = 1, 1

    for i in range(3, n + 1):
        rabbits[i] = rabbits[i - 1] + k * rabbits[i - 2]

    return rabbits[n]

with open("./rosalind_fib.txt", "r") as f:
    n, k = map(int, f.readline().split())
    total_num = rabbit_pairs(n, k)
    print(total_num)
