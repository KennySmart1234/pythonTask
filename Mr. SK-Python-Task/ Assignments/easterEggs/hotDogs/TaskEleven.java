



year = int(print("Enter number of Years: "))


double birth = 365 * 24 * 60 * 60 / 7
double death = 365 * 24 * 60 * 60 / 13
double immigrant = 365 * 24 * 60 * 60 / 45

int current_population = 312032486
double population_total = current_population + birth + immigrant - death
double population_after = population_total * year
            
print("Population after:" + population_after + "\n")


