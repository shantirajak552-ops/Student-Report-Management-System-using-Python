name = input ("enter the name")
marks = {}

for i in range(3):
    subject  = input("Enter subject name: ")
    num = int(input("Enter marks: "))
    marks[subject] = num

total = sum(marks.values())
average = sum(marks.values()) / len(marks)
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = " C"
else :
    grade = " D"

print("name", name)
print(" marks", marks)
print("total", total)
print("average", average)
print("grade", grade)
