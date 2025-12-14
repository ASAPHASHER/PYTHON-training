import os

class Student:
    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

    def grade(self):
        avg = self.average()
        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 60:
            return "C"
        else:
            return "D"

def save_student(student):
    with open("students.txt", "a") as file:
        marks = ",".join(map(str, student.marks))
        file.write(f"{student.student_id}|{student.name}|{marks}\n")

def load_students():
    students = []
    if not os.path.exists("students.txt"):
        return students

    with open("students.txt", "r") as file:
        for line in file:
            sid, name, marks = line.strip().split("|")
            marks = list(map(int, marks.split(",")))
            students.append(Student(sid, name, marks))
    return students

def display_students(students):
    for s in students:
        print(f"ID: {s.student_id}")
        print(f"Name: {s.name}")
        print(f"Average: {s.average():.2f}")
        print(f"Grade: {s.grade()}")
        print("-" * 20)

def main():
    while True:
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            sid = input("Student ID: ")
            name = input("Name: ")
            marks = []
            for i in range(3):
                mark = int(input(f"Enter mark {i+1}: "))
                marks.append(mark)
            student = Student(sid, name, marks)
            save_student(student)

        elif choice == "2":
            students = load_students()
            display_students(students)

        elif choice == "3":
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
