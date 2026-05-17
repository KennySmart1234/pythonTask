



number = int(input("Enter an integer: "))
count = 0
total_sum = 0
product = 1
largest = 0
smallest = 0

while count < 4:  
    count = count + 1
    product = product * number
    total_sum = total_sum + number
    if number >= largest:
        largest = number
    if number <= smallest:
        smallest = number
    if count == 4:
        break
    number = int(input("Enter an integer: "))

print("Sum: ", total_sum)
print("Average ", total_sum/count)
print("Product ", product)
print("Largest ", largest)
print("Smallest ", smallest)





#largest = number
#if number > largest:
#    largest == numberone
#if numbertwo > largest:
#    largest == numbertwo
#if numberthree > largest:
#    largest == numberthree
#if numberfour > largest:
#    largest == numberfour
#print(largest)


