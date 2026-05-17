




student_name = input("Enter your name: ")
student_score = int(input("Enter your score: "))

count = 0
total_score = 0
while student_score != -1:
    count = count + 1
    total_score = total_score + student_score
    student_score = int(input("Enter your score: "))
    if student_score == None:
        print(done)

print(student_name, "Average:", total_score/count)











