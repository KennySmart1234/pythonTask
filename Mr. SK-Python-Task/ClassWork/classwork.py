name = input("Enter your name ")
age = input("what is your age ")

age = int(age)

print("your name is ", name, "and your", (age + 10), "years old")


comment = """ your name is ", name, "and your", (age + 10), "years old """

print(comment)


name = input("Enter your name ")
age = input("what is your age ")

age = int(age)
if name != "":

    print("your name is ", name, "and your", (age + 10), "years old")
else:
    print("Invalid name")
