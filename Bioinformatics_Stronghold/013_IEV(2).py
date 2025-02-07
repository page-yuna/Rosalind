### Calculating Expected Offspring
# ID: IEV
# Topics: Heredity, Probability

# Given: Six nonnegative integers, each of which does not exceed 20,000.
#        The integers correspond to the number of couples in a population
#        possessing each genotype pairing for a given factor.
#        In order, the six given integers represent the number of couples having the following genotypes:
# Return: The expected number of offspring displaying the dominant phenotype in the next generation,
#        under the assumption that every couple has exactly two offspring.

# Sample Dataset: "1 0 0 1 0 1"
# Sample Output: "3.5"


from itertools import product

def geno_unique_comb(alleles):
    combs = set()
    for p1 in product(alleles, repeat=2):
        for p2 in product(alleles, repeat=2):
            parent1, parent2 = "".join(sorted(p1)), "".join(sorted(p2))
            combined = tuple(sorted([parent1, parent2]))
            combs.add(combined[0] + "_" + combined[1])
            
    return sorted(list(combs))

def cal_offspring(p_genotype):
    offspring = 0
    for geno, count in p_genotype.items():
        parent1, parent2 = geno.split("_")
        if parent1 == "AA": offspring += 2 * count
        elif parent1 == "Aa" and parent2 == "Aa": offspring += 1.5 * count
        elif parent1 == "Aa" and parent2 == "aa": offspring += 1 * count

    return offspring

def main():
    alleles = ['A', 'a']
    geno_comb = geno_unique_comb(alleles)
    
    fpath = "./rosalind_iev.txt"
    with open(fpath, 'r') as f:
        data = f.read()
        
    p_genotype = {}
    geno_list, num_list = geno_comb, data.split(' ')
        
    for i in range(len(geno_list)):
        geno = geno_list[i]
        num = int(num_list[i]) if i < len(num_list) else 0
        p_genotype[geno] = num

    offspring = cal_offspring(p_genotype)

    if offspring.is_integer():
        print(int(offspring))
    else:
        print(offspring)
    

if __name__ == "__main__":
    main()
