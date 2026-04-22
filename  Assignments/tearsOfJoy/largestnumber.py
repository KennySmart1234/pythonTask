



while True:
    user_input = input("Enter a number: ")

    if user_input == "done":
        break

    try:
        user_input = int(user_input)
        largest_number = 0
        if user_input > largest_number:
            largest_number = user_input
    except invalid_input:
        print("invalid input ")

print(largest_number) 



















