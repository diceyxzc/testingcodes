import rewrite

class Course_Outline_Input:
    def get_student_outline(self):
        obj2 = rewrite.Course_Outline()
        total_subjects = int(input("Enter the Number of Subjects: "))
        subjects = []

        for i in range(total_subjects):
            subject = input(f"Enter Subject {i + 1}: ")
            units = int(input(f"Enter No.s of Unit {i + 1}: "))
            section = input(f"Enter Section for the Subject {i + 1}: ")
            course_outline = rewrite.Course_Outline()
            course_outline.get_student_outline(total_subjects, section, units, subject)
            subjects.append(course_outline)

        obj2.total_units_calculation(units)
        obj2.display_student_outline(subjects)

a = Course_Outline_Input()
a.get_student_outline()