


def validate_email(email):
    email_length = len(email_address)


    if email_length >= 8:
        if "@" in email:
            if email[0] !="@" and email[-1] !="@":
                print("Valid email")

    else:
        ("Invalid email!!! Check your input") 
            
email_address = input("Enter your email address: ")
validate_email(email_address)
    
