


largest_number = None
while True:
    user_input = input("Enter a number: ")
    if user_input == "done":
        break

    user_input = int(user_input)
    if largest_number is None or user_input > largest_number:
        largest_number = user_input

print("Largest: ", largest_number) 



















