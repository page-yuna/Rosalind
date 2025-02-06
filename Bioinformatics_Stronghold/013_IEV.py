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


data = "19305,19165,18099,17624,16783,16532"

p_genotype = {}
geno_list, num_list = ['AA_AA', 'AA_Aa', 'AA_aa', 'Aa_Aa', 'Aa_aa', 'aa_aa'], data.split(',')
for i in range(len(geno_list)):
    geno, num = geno_list[i], num_list[i]
    p_genotype[geno] = num

def cal_offspring(p_genotype):
    offspring = 0
    for geno in p_genotype:
        if int(p_genotype[geno]) > 0:
            if geno in ('AA_AA', 'AA_Aa', 'AA_aa'):
                offspring += 2 * int(p_genotype[geno])
            elif geno == 'Aa_Aa':
                offspring += 1.5 * int(p_genotype[geno])
            elif geno == 'Aa_aa':
                offspring += 1 * int(p_genotype[geno])
    
    return offspring

offspring = cal_offspring(p_genotype)
print(offspring)
