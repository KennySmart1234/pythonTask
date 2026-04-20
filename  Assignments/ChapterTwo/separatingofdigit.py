number_input = input("Enter five digit input: ")

number_input = int(number_input)


remainder_one = number_input % 10
division_one = number_input // 10


remainder_two = division_one % 10
division_two = division_one // 10


remainder_three = division_two % 10
division_three = division_two // 10


remainder_four = division_three % 10
division_four = division_three // 10


remainder_five = division_four % 10
division_five = division_four // 10



print(remainder_five, "   ", remainder_four, "   ", remainder_three, "   ", remainder_two, "   ", remainder_one)





