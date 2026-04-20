

number = int(input("Enter a number: "))


for numbers in range(1, number):
    for order in range(1, number):

        print(numbers * order, end = "     ")

    print("       ")

