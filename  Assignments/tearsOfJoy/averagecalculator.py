

number = int(input("Enter a number: "))
total_number = 0
count = 0
while number != -1:

    count = count + 1
    total_number = total_number + number
    number = int(input("Enter a number: "))



print("Count", count)
print("Average:", total_number/count)

















