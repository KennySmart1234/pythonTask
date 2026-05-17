


password = "python123" 
count = 0
while True:
    user_input = input("Enter your password: ")
    if user_input == password:
        print("Access granted")
        break;    
    if user_input != password:
        count = count + 1
        print("Wrong password")
        if count == 3:
            break;








