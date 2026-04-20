""" 
create a program that evaluates password 
based on its lenght
prompt the user to create a password
analyze it lenth 
classify base on One to four categories very weak, weak, strong, or very strong"""




password = input("Enter password: ")
#    print(password)

password_length = len(password)


if password_length < 8:
    print("Very weak")
if password_length == 8:
    print("Weak")
if password_length > 8 or password_length == 16:
    print("Strong")
if password_length > 16:
    print("Very Strong")











