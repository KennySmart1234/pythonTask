
digit_input = int(input(print("Enter a any digit between 0 - 1000: ")))

division_digit = digit_input % 10
division_digit_one = digit_input / 10


division_digit_two = division_digit_one % 10
division_result = division_digit_one / 10


division_digit_three = division_result % 10
division_digit = division_result / 10
               


print(division_digit_three, division_digit_two, division_digit, "\n")

print(division_digit_three + division_digit_two + division_digit)




