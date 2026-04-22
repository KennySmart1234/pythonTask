

def largest_number(number_one, number_two, number_three):
    largest = number_one
    if number_two > largest:
        largest = number_two
    if number_three > largest:
        largest = number_three
    return largest


print(largest_number(10, 44, 3))




















