

number = int(input("Enter a number: "))


for numbers in range(1, number +1):
    print(numbers, end =" | ")
    for order in range(1, number +1):
        print(f"{numbers * order}\t", end ="-")

    print("")

