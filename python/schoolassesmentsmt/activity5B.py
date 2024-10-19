import activity5

class Student_Info_Input:
    
    def get_student_input(self):
        obj = activity5.Student_Info()
        name = input("Student Name: ")
        course = input("Student Course: ")
        number = input("Student Number: ")
        academic_year = input("Academic Year: ")
        printed_date = input("Date Printed: ")

        student_data = obj.get_student_data(name, course, number, academic_year, printed_date)
        obj.display_student_data()

class Course_Outline_Input:
    def get_student_outline(self):
        obj2 = activity5.Course_Outline()
        units = int(input("Enter the Number of Subjects: "))
        subjects = []

        for i in range(units):
            subject = input(f"Enter Subject {i + 1}: ")
            section = input(f"Enter Section for the Unit {i + 1}: ")
            course_outline = activity5.Course_Outline()
            course_outline.get_student_outline(section, subject, 1)
            subjects.append(course_outline)

        obj2.display_student_outline(subjects)

a = Student_Info_Input()
a.get_student_input()

a = Course_Outline_Input()
a.get_student_outline()
