'''initialize variables count, pass, fail
promt the user to enter score
check if the score is valid(1 f0r pass and 2 for fail)
if any of the above is correct add it to variabe created
terminate if valid scores = 10 
'''

count = 0
passes = 0
failure = 0

grade = int(input("Enter 1 for pass or 2 for fail "))

while count < 10:
    if grade == 1:
        count = count + 1
        passes = passes + 1
    if grade == 2:
        failure = failure + 1
    grade = int(input("Enter 1 for pass or 2 for fail "))

print("Total Passes: ", passes)
print("Total Failure: ", failure)
print("Total Count: ", failure + passes)
