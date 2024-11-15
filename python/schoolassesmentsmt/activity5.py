class Student_Info:
    def __init__(self):
        self.student_name = ""
        self.student_course = ""
        self.student_number = ""
        self.academic_year = ""
        self.printed_date = ""

    def get_student_data(self, student_name, student_course, student_number, academic_year, printed_date):
        self.student_name = student_name
        self.student_course = student_course
        self.student_number = student_number
        self.academic_year = academic_year
        self.printed_date = printed_date

    def display_student_data(self):
        width = 91
        print("-" * width)
        print(f"| NAME: \t: {self.student_name} \t\t STUDENT NO.\t: {self.student_number} \t  |")
        print(f"| COURSE: \t: {self.student_course} \t\t\t\t ACAD. YEAR \t: {self.academic_year} \t  |")
        print(f"| DATE: \t: {self.printed_date} \t\t\t\t\t\t\t  |")
        print("-" * width)

class Course_Outline:
    def __init__(self):
        self.student_section = ""
        self.student_subject = ""
        self.student_units = 0.00
        self.tuition_fee_lecture = 1551.00
        self.unit_tuition_fee = 0.00
    
    def get_student_outline(self, student_section, student_subject, student_units):
        self.student_section = student_section
        self.student_subject = student_subject
        self.student_units = student_units

    def tuition_fee_calculation(self, student_units, tuition_fee_lecture):
        self.unit_tuition_fee = student_units * tuition_fee_lecture
        return self.unit_tuition_fee

    def display_student_outline(self, subjects):
        width = 50
        print("-" * width)
        for i, course_outline in enumerate(subjects, start=1):
            print(f"Subject Code: {course_outline.student_subject} \t| Section: {course_outline.student_section}")
        print("-" * width)
        print(f"{self.unit_tuition_fee}")

class Assessment_Amount:
    def __init__(self):
        self.adu_chronical = 0.00
        self.athletic = 0.00
        self.audio_visual_library = 0.00
        self.ausg = 0.00
        self.cultural_fee = 0.00
        self.energy_cost = 0.00
        self.guidance = 0.00
        self.insurance_fee = 0.00
        self.learning_management_system = 0.00
        self.library_fee = 0.00
        self.medical_dental = 0.00
        self.registration = 0.00
        self.rso = 0.00
        self.student_activities = 0.00
        self.student_nurturance = 0.00
        self.technology_fee = 0.00
        self.test_papers = 0.00
        self.other_assessment = 0.00
        self.downpayment = 0.00
        self.total_due = 0.00
        self.prelim = 0.00
        self.midterm = 0.00
        self.final = 0.00
    
    def get_student_assesssment(self, adu_chronical, athletic, audio_visual_library,
                                ausg, cultural_fee, energy_cost, guidance, insurance_fee,
                                learning_management_system, library_fee, medical_dental,
                                registration, rso, student_activities, student_nurturance,
                                technology_fee, test_papers, downpayment):
        
        self.adu_chronical = adu_chronical
        self.athletic = athletic
        self.audio_visual_library = audio_visual_library
        self.ausg = ausg
        self.cultural_fee = cultural_fee
        self.energy_cost = energy_cost
        self.guidance = guidance
        self.insurance_fee = insurance_fee
        self.learning_management_system = learning_management_system
        self.library_fee = library_fee
        self.medical_dental = medical_dental
        self.registration = registration
        self.rso = rso
        self.student_activities = student_activities
        self.student_nurturance = student_nurturance
        self.technology_fee = technology_fee
        self.test_papers = test_papers

        self.other_assessment = (adu_chronical + athletic + audio_visual_library + ausg + cultural_fee 
        + energy_cost + guidance + insurance_fee + learning_management_system + library_fee + medical_dental 
        + registration + rso + student_activities + student_nurturance + technology_fee + test_papers)

        self.total_due = self.other_assessment - downpayment
        self.downpayment = downpayment

        return {
            "other_assessment": self.other_assessment,
            "total_due": self.total_due
        }
    
    def three_terms_total(self, total_due):
        term_amount = total_due / 3
        self.prelim = term_amount
        self.midterm = term_amount
        self.final = term_amount

        return {
            "prelim": self.prelim,
            "midterm": self.midterm,
            "final": self.final
        }

    
    def display_assessment(self):
        print("\nAssessment Input Summary:")
        print(f"Adu Chronical: {self.adu_chronical:.2f}")
        print(f"Athletic Fee: {self.athletic:.2f}")
        print(f"Audio Visual Library Fee: {self.audio_visual_library:.2f}")
        print(f"AUSG Fee: {self.ausg:.2f}")
        print(f"Cultural Fee: {self.cultural_fee:.2f}")
        print(f"Energy Cost: {self.energy_cost:.2f}")
        print(f"Guidance Fee: {self.guidance:.2f}")
        print(f"Insurance Fee: {self.insurance_fee:.2f}")
        print(f"Learning Management System Fee: {self.learning_management_system:.2f}")
        print(f"Library Fee: {self.library_fee:.2f}")
        print(f"Medical Dental Fee: {self.medical_dental:.2f}")
        print(f"Registration Fee: {self.registration:.2f}")
        print(f"RSO Fee: {self.rso:.2f}")
        print(f"Student Activities Fee: {self.student_activities:.2f}")
        print(f"Student Nurturance Fee: {self.student_nurturance:.2f}")
        print(f"Technology Fee: {self.technology_fee:.2f}")
        print(f"Test Papers Fee: {self.test_papers:.2f}")
        print(f"Assessment Amount: {self.other_assessment:.2f}")
        print(f"Downpayment: {self.downpayment:.2f}")
        print(f"Total Due: {self.total_due:.2f}")
        print(f"Prelim Fee: {self.prelim:.2f}")
        print(f"Midterm Fee: {self.midterm:.2f}")
        print(f"Final Fee: {self.final:.2f}")
