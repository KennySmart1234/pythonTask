input_one = input("Enter an integer: ")
input_two = input("Enter another integer: ")
input_three = input("Enter another integer: ")


input_one = int(input_one)
input_two = int(input_two) 
input_three = int(input_three)


total_sum = (input_one + input_two + input_three)
average = total_sum/2

largest = input_one
if input_two > largest: 
    largest = input_two
if input_three > largest:
    largest = input_three

smallest = input_one
if input_two < smallest: 
    smallest = input_two
if input_three < smallest:
    smallest = input_three



print("Sum: ", total_sum)
print("Average: ", average)
print("Largest", largest)
print("smallest", smallest)










