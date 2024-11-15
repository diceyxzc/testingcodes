import rewrite

class Student_Info_Input:
    
    def get_student_input(self):
        obj = rewrite.Student_Info()
        name = input("Student Name: ")
        course = input("Student Course: ")
        number = input("Student Number: ")
        academic_year = input("Academic Year: ")
        printed_date = input("Date Printed: ")

        student_data = obj.get_student_data(name, course, number, academic_year, printed_date)
        obj.display_student_data()

a = Student_Info_Input()
a.get_student_input()