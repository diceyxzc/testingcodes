import rewriteexperiemtn

class Student_Info_Input:
    
    def get_student_input(self):
        obj = rewriteexperiemtn.Student_Info()
        print("| STUDENT INFORMATION |")
        name = input("Student Name: ")
        course = input("Student Course: ")
        number = input("Student Number: ")
        academic_year = input("Academic Year: ")
        printed_date = input("Date Printed: ")

        total_subjects = int(input("Enter the Number of Subjects: "))
        subjects = []

        for i in range(total_subjects):
            subject = input(f"Enter Subject {i + 1}: ")
            units = int(input(f"Enter No.s of Unit {i + 1}: "))
            section = input(f"Enter Section for the Subject {i + 1}: ")
            course_outline = rewriteexperiemtn.Student_Info()
            course_outline.get_course_outline(total_subjects, section, units, subject)
            subjects.append(course_outline)

        student_data = obj.get_student_data(name, course, number, academic_year, printed_date)
        obj.display_student_data()
        obj.total_units_calculation(subjects)
        obj.display_student_outline(subjects)

student_info = Student_Info_Input()
student_info.get_student_input()