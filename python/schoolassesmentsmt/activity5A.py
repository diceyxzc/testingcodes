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

class Assessment_Input:

    def get_assessment_input(self):
        obj3 = activity5.Assessment_Amount()
        adu_chronical = input("Enter Adu Chronical: ")
        athletic = float(input("Enter Athletic Fee: "))
        audio_visual_library = float(input("Enter Audio Visual Library Fee: "))
        ausg = float(input("Enter AUSG Fee: "))
        cultural_fee = float(input("Enter Cultural Fee: "))
        energy_cost = float(input("Enter Energy Cost: "))
        guidance = float(input("Enter Guidance Fee: "))
        insurance_fee = float(input("Enter Insurance Fee: "))
        learning_management_system = float(input("Enter Learning Management System Fee: "))
        library_fee = float(input("Enter Library Fee: "))
        medical_dental = float(input("Enter Medical Dental Fee: "))
        registration = float(input("Enter Registration Fee: "))
        rso = float(input("Enter RSO Fee: "))
        student_activities = float(input("Enter Student Activities Fee: "))
        student_nurturance = float(input("Enter Student Nurturance Fee: "))
        technology_fee = float(input("Enter Technology Fee: "))
        test_papers = float(input("Enter Test Papers Fee: "))
        other_assessment = float(input("Enter Other Assessment Fee: "))
        downpayment = float(input("Enter Downpayment: "))
        prelim = float(input("Enter Prelim Fee: "))
        midterm = float(input("Enter Midterm Fee: "))
        final = float(input("Enter Final Fee: "))

        student_assessment = obj3.get_student_assesssment(
            adu_chronical, athletic, audio_visual_library, ausg, cultural_fee, energy_cost,
            guidance, insurance_fee, learning_management_system, library_fee, medical_dental,
            registration, rso, student_activities, student_nurturance, technology_fee, test_papers,
            other_assessment, downpayment, prelim, midterm, final
        )
        obj3.display_assessment()


a = Student_Info_Input()
a.get_student_input()

a = Course_Outline_Input()
a.get_student_outline()

a = Assessment_Input()
a.get_assessment_input()