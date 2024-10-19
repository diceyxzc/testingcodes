import activity5
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

a = Assessment_Input()
a.get_assessment_input()
