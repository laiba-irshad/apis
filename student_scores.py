# Step 1: OOP - a Student class with a name and a score
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

# Step 2: List - store 3 students in one list
students = [
    Student("Ali", 72),
    Student("Sara", 45),
    Student("Ahmed", 88),
]

# Step 5: Function - returns the student with the highest score
def top_scorer(student_list):
    best = student_list[0]            # start by assuming the first is best
    for student in student_list:      # check every student
        if student.score > best.score:
            best = student            # found someone higher, so update
    return best

# Steps 3 & 4: Loop + If - visit every student, show only scores above 50
print("Students who passed (score above 50):")
for student in students:
    if student.score > 50:
        print(f"{student.name}: {student.score}")

# Find and show the top scorer
top = top_scorer(students)
print(f"\nTop scorer: {top.name} with {top.score}")