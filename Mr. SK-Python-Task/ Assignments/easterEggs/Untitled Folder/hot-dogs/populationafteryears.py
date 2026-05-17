



year = int(input(print("Enter number of Years: ")))


birth = 365 * 24 * 60 * 60 / 7
death = 365 * 24 * 60 * 60 / 13
immigrant = 365 * 24 * 60 * 60 / 45

current_population = 312032486
population_total = current_population + birth + immigrant - death
population_after = population_total * year
            
print("Population after:", population_after , "\n")


