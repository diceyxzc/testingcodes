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
        print(f"| NAME \t: {self.student_name}  \t\t STUDENT NO.\t: {self.student_number} \t  |")
        print(f"| COURSE \t: {self.student_course}  \t\t\t\t ACAD. YEAR \t: {self.academic_year} \t  |")
        print(f"| DATE \t: {self.printed_date}  \t\t\t\t\t\t\t  |")
        print("-" * width)

class Course_Outline:    
    def __init__(self):
        self.student_section = ""
        self.student_subject = ""
        self.student_total_subjects = 0.00
        self.student_units = 0.00
        self.total_units = 0.00
            
    def get_student_outline(self, student_total_subjects, student_section, student_units, student_subject):
        self.student_total_subjects = student_total_subjects
        self.student_section = student_section
        self.student_units = student_units
        self.student_subject = student_subject
    
    def total_units_calculation(self, units):
        for i in range(0, units + 1):
           self.total_units += units
        return self.total_units

    def display_student_outline(self, subjects):
        width = 66
        print("-" * width)
        for i, course_outline in enumerate(subjects, start=1):
            print(f"| Section: {course_outline.student_section} \t| Subject: {course_outline.student_subject} \t\t| Units: {course_outline.student_units}\t\t |")
        print(f"|\t\t|\t\t\t| Total Units: {self.total_units:.0f} \t | ")
        print("-" * width)

class Assessment_Amount:
    tuition_fee_lecture = 1551.00
    
    def __init__(self):
        self.tuition_fee_lecture = 1551.00
        self.total_units = 0.00
        self.tuition_fee_lecture_total = 0.00
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
    
    def get_tuition_fee_lecture(self, total_units):
        self.tuition_fee_lecture_total = total_units * 1551
        return self.tuition_fee_lecture_total

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

        self.other_assessment = (self.tuition_fee_lecture_total + adu_chronical + athletic + audio_visual_library + ausg + cultural_fee 
        + energy_cost + guidance + insurance_fee + learning_management_system + library_fee + medical_dental 
        + registration + rso + student_activities + student_nurturance + technology_fee + test_papers)

        self.downpayment = downpayment
        self.total_due = self.other_assessment - downpayment

        term_amount = round((self.other_assessment - downpayment) / 3, 2)
        remainder = round((self.other_assessment - downpayment) - (term_amount * 3), 2)
        
        self.prelim = term_amount
        self.midterm = term_amount
        self.final = term_amount + remainder

        return self.other_assessment, self.total_due, self.prelim, self.midterm, self.final
        
    def display_assessment(self):
        print("\nAssessment Input Summary:")
        print(f"Tuition Fee Lecture \t\t: {self.tuition_fee_lecture:.2f}")
        print(f"Adu Chronical \t\t\t: {self.adu_chronical:.2f}")
        print(f"Athletic Fee \t\t\t: {self.athletic:.2f}")
        print(f"Audio Visual Library Fee \t: {self.audio_visual_library:.2f}")
        print(f"AUSG Fee \t\t\t: {self.ausg:.2f}")
        print(f"Cultural Fee \t\t\t: {self.cultural_fee:.2f}")
        print(f"Energy Cost \t\t\t: {self.energy_cost:.2f}")
        print(f"Guidance Fee \t\t\t: {self.guidance:.2f}")
        print(f"Insurance Fee \t\t\t: {self.insurance_fee:.2f}")
        print(f"Learning Management System Fee \t: {self.learning_management_system:.2f}")
        print(f"Library Fee \t\t\t: {self.library_fee:.2f}")
        print(f"Medical Dental Fee \t\t: {self.medical_dental:.2f}")
        print(f"Registration Fee \t\t: {self.registration:.2f}")
        print(f"RSO Fee \t\t\t: {self.rso:.2f}")
        print(f"Student Activities Fee \t\t: {self.student_activities:.2f}")
        print(f"Student Nurturance Fee \t\t: {self.student_nurturance:.2f}")
        print(f"Technology Fee \t\t\t: {self.technology_fee:.2f}")
        print(f"Test Papers Fee \t\t: {self.test_papers:.2f}")
        print(f"Assessment Amount \t\t: {self.other_assessment:.2f}")
        print(f"Downpayment \t\t\t: {self.downpayment:.2f}")
        print(f"Total Due \t\t\t: {self.total_due:.2f}")
        print(f"Prelim Fee \t\t\t: {self.prelim:.2f}")
        print(f"Midterm Fee \t\t\t: {self.midterm:.2f}")
        print(f"Final Fee \t\t\t: {self.final:.2f}")