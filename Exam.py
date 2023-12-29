
students = [
    (101, 'Alok'),
    (102, 'Arun'),
    (103, 'Ashish'),
    (104, 'Roshani'),
    (105, 'Eva'),
]


sorted_students = sorted(students, key=lambda student: student[1])


for roll_no, name in sorted_students:
    print(f"Roll No: {roll_no},Name:{name}")