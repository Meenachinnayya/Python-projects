# Student Marks Calculator

name = input("Enter student name: ")

mark1 = int(input("Enter Tamil mark: "))
mark2 = int(input("Enter English mark: "))
mark3 = int(input("Enter Python mark: "))

total = mark1 + mark2 + mark3
average = total / 3

print("\n----- STUDENT REPORT -----")
print("Student Name:", name)
print("Total Marks:", total)
print("Average:", average)

if mark1 >= 35 and mark2 >= 35 and mark3 >= 35:
    print("Result: PASS")
else:
    print("Result: FAIL")
