class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married
    
    def introduce_myself(self):
        print(f"Full Name: {self.fullname}")
        print(f"Age: {self.age}")
        print(f"Marital Status: {'Married' if self.is_married else 'Single'}")
        

class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks
    
    def calculate_average_mark(self):
        total_marks = sum(self.marks.values())
        num_subjects = len(self.marks)
        return total_marks / num_subjects


class Teacher(Person):
    def __init__(self, fullname, age, is_married, experience, salary):
        super().__init__(fullname, age, is_married)
        self.experience = experience
        self.salary = salary
    
    def calculate_salary(self):
        standard_salary = self.salary
        bonus_percentage = max(0, (self.experience - 3) * 0.05)
        bonus_amount = standard_salary * bonus_percentage
        total_salary = standard_salary + bonus_amount
        return total_salary


def create_students():
    student1 = Student("Johne Depp", 18, False, {"Math": 3, "Science": 4, "History": 4})
    student2 = Student("Leonardo De Kaprio", 17, False, {"Math": 4, "Science": 3, "History": 4})
    student3 = Student("Tashiev Bayel", 16, False, {"Math": 6, "Science": 6, "History": 6})
    
    students = [student1, student2, student3]
    return students


students_list = create_students()

for student in students_list:
    student.introduce_myself()
    print("Marks:")
    for subject, mark in student.marks.items():
        print(f"{subject}: {mark}")
    average_mark = student.calculate_average_mark()
    print(f"Average Mark: {average_mark}")
    print()


teacher = Teacher("Rassul", 35, True, 7, 5000)
teacher.introduce_myself()
teacher_salary = teacher.calculate_salary()
print(f"Salary: {teacher_salary}")
