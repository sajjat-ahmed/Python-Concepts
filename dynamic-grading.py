subject = input("Submit your subject name? ")
grade = int(input("What was your score? "))

if grade >= 80 and grade <= 100:
    print(f"{subject} {grade} A+")
elif grade >= 70 and grade <= 79:
    print(f"{subject} {grade} A-")
elif grade >= 60 and grade <= 69:
    print(f"{subject} {grade} A")
elif grade >= 50 and grade <= 59:
    print(f"{subject} {grade} B")
elif grade >= 40 and grade <= 49:
    print(f"{subject} {grade} C")
elif grade >= 33 and grade <= 39:
    print(f"{subject} {grade} D")
else:
    print(f"{subject} {grade} F")