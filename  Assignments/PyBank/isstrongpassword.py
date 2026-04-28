
def is_strong_password(password_length):
    password = input("Enter your password: ")

    password_length = len(password)

    if password_length >= 8:
        return True
    else:
        return False

print(is_strong_password)




