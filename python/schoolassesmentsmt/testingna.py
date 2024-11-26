import rewriteexperiemtn

class Student_Info_Input:
    
    def get_student_input(self):
        obj = rewriteexperiemtn.Student_Info()
        obj2 = rewriteexperiemtn.Assessment_Amount()
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

        print("| STUDENT ASSESSMENT |")
        total_units = int(input("Enter Total Units: "))
        adu_chronical = float(input("Enter Adu Chronical: "))
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
        downpayment = float(input("Enter Downpayment: "))

        student_data = obj.get_student_data(name, course, number, academic_year, printed_date)
        obj.display_student_data()
    
        total_of_units = obj2.get_tuition_fee_lecture(total_units)

        student_assessment = obj2.get_student_assesssment(adu_chronical, athletic, audio_visual_library, ausg, cultural_fee, energy_cost, guidance, 
                                                  insurance_fee, learning_management_system, library_fee, medical_dental, registration, rso, 
                                                  student_activities, student_nurturance, technology_fee, test_papers, downpayment)

        obj.total_units_calculation(subjects)
        obj.display_student_outline(subjects)
        obj2.display_assessment()

student_info = Student_Info_Input()
student_info.get_student_input()
