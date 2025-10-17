
student = {
    "name": "Alice Johnson",
    "roll_number": "23CS45",
    "register_number": "2025001234",
    "department": "Computer Science",
    "semester": 5
}


student["total_mark"] = int(input("enter the mark"))

mark = student["total_mark"]
if mark >= 90:
    grade = "A"
elif mark >= 82:
    grade = "B"
elif mark >= 75:
    grade = "C"
elif mark >= 60:
    grade = "D"
elif mark >= 50:
    grade = "P"
else:
    grade = "F"


student["grade"] = grade


del student["roll_number"]


print("Student Details:", student)
