student1_name = "Dorothy"
student1_grade = "1.5"
student1_subject = "Algebra"

student2_name = "Marcus"
student2_grade = "2.0"
student2_subject = "Physics"

student3_name = "Murmansk"
student3_grade = "3.0"
student3_subject = "English"

def print_student_info_function(name, grade, subject):
    print(f"Student {name} - grade is {grade} - subject is {subject}")

if __name__ == "__main__":
    print_student_info_function(student1_name, student1_grade, student1_subject)
    print_student_info_function(student2_name, student2_grade, student2_subject)
    print_student_info_function(student3_name, student3_grade, student3_subject)

#ALL METHODS ARE FUNCTIONS, BUT NOT ALL FUNCTIONS ARE METHOD

class Student: #CLASS IS THE BLUEPRINT FOR CREATING AN OBJECT
    default_subject = "Basic Electronics"
    year_and_section = "1-2"


    def __init__(self, name, grade, subject): #constructor
        self.name = name #property
        self.grade = grade #property
        self.subject = subject #property

    def print_student_info_method(self):
        print(f"Student {self.name} - grade is {self.grade} - subject is {self.subject}")

    @classmethod
    def create_student_with_default_info(cls, name, grade):
        print(f"Student {name} - grade is {grade} - subject is {cls.default_subject}")
        return cls(name, grade, cls.default_subject)

    @classmethod
    def update_year_and_section(cls, year_section_update):
        cls.year_and_section = year_section_update


    @staticmethod
    def is_passing_grade(grade):
        if grade <= 3.0:
            print("Passed")
        else:
            print("Failed")

#-------------------------------------
print("=====================================")

if __name__ == "__main__":
    student1 = Student("Dorothy", 1.0, "Engineering")
    student2 = Student("Anthony", 2.0, "Culinary Arts")
    student3 = Student("Zara", 3.0, "Telecomms")
    student4 = Student.create_student_with_default_info("Doro", 1.5)


    student1.print_student_info_method()
    student2.print_student_info_method()
    student3.print_student_info_method()

    Student.is_passing_grade(5.0)
    Student.is_passing_grade(student1.grade)
    Student.is_passing_grade(student2.grade)
    Student.is_passing_grade(student3.grade)
    Student.is_passing_grade(student4.grade)

    print(student1.year_and_section)
    print(student2.year_and_section)
    print(student3.year_and_section)
    print(student4.year_and_section)
    Student.update_year_and_section("2-2")
    print(student1.year_and_section)
    print(student2.year_and_section)
    print(student3.year_and_section)
    print(student4.year_and_section)