### Mortal Fibonacci Rabbits
# ID: FIBD
# Topic: Combinatorics, Dynamic Programming

# Given: Positive integers n≤100 and m≤20.
# Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.

# Sample Dataset: "6 3"
# Sample Output: "4"

# url: https://rosalind.info/problems/fibd/


def mortal_fibo_rabbits(n, m):
    rabbits = [0] * m
    rabbits[0] = 1

    for month in range(1, n):
        offspring = sum(rabbits[1:])
        for i in range(m-1, 0, -1):
            rabbits[i] = rabbits[i - 1]

        rabbits[0] = offspring

    return sum(rabbits)

n, m = ??
result = mortal_fibo_rabbits(n, m)
print(result)
