'''creating a script that plays the part of the independent computer
giving its user a simple medical diagnosis. 
The script should prompt the user with 'What is your problem?'
When the user answers and presses Enter, 
the script should simply ignore the user’s input,
then prompt the user again with 
'Have you had this problem before (yes or no)?' 
If the user enters 'yes', 
print 'Well, you have it again.' 
If the user answers 'no', 
print 'Well, you have it now.'''



medical_problem = input("What is your problem? ")


if medical_problem != " ":
    users_response = input("Have you had this problem before (yes or no)?")
    if users_response == "yes":
        print("Well, you have it again")
    if users_response == "no":
        print("Well, you have it now")
















