# Simple Student Grading System

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def show_result(self):
        if self.grades:
            avg = sum(self.grades) / len(self.grades)
            print(f"{self.name}: Grades = {self.grades}, Average = {avg:.2f}")
        else:
            print(f"{self.name}: No grades recorded.")

# Create student objects
michel = Student("Michel")
jane = Student("Jane")

# Record grades
michel.add_grade(85)
michel.add_grade(90)
jane.add_grade(0)

# Show results
michel.show_result()
jane.show_result()