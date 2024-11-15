class Student_Info:
    tuition_fee_lecture = 1551.00
    
    def __init__(self):
        self.student_name = ""
        self.student_course = ""
        self.student_number = ""
        self.academic_year = ""
        self.printed_date = ""
        self.student_section = ""
        self.student_subject = ""
        self.student_total_subjects = 0.00
        self.student_units = 0.00
        self.total_units = 0.00
        self.tuition_fee_lecture = 1551.00
        self.unit_tuition_fee = 0.00

    def get_student_data(self, student_name, student_course, student_number, academic_year, printed_date):
        self.student_name = student_name
        self.student_course = student_course
        self.student_number = student_number
        self.academic_year = academic_year
        self.printed_date = printed_date
    
    def get_student_outline(self, student_total_subjects, student_section, student_units, student_subject):
        self.student_total_subjects = student_total_subjects
        self.student_section = student_section
        self.student_units = student_units
        self.student_subject = student_subject

    def total_units_calculation(self, subjects):
        for i, course_outline in enumerate(subjects, start=1):    
            self.total_units += int(sum({course_outline.student_units}))
        return self.total_units

    def display_student_data(self):
        width = 82
        name_width = 35
        number_width = 15
        course_width = 35
        year_width = 15

        print("-" * width)
        print(f"| NAME   : {self.student_name:<{name_width}} | STUDENT NO. : {self.student_number:<{number_width}}   |")
        print(f"| COURSE : {self.student_course:<{course_width}} | ACAD. YEAR  : {self.academic_year:<{year_width}}   |")
        print("-" * width)

    
    def display_student_outline(self, subjects):
        width = 82
        subject_width = 30
        section_width = 8
        date_width = 20
        print("|\t  SECTION   \t \t      SUBJECT      \t   \t        UNITS    |")
        print("-" * width)
        for i, course_outline in enumerate(subjects, start=1):
            print(f"|\t  {course_outline.student_section:<{section_width}} \t  {course_outline.student_subject:<{subject_width}}   \t\t  {course_outline.student_units}\t |")
        print(f"|\t\t\t \t\t\t\t    Total Units: {self.total_units:.0f} \t | ")
        print("-" * width)
        print(f"| DATE PRINTED \t: {self.printed_date:<{date_width}} \t\t\t\t\t\t |")
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
        line_length = 47
        width = 12
        print("-" * 48)
        print("|\t       ASSESSMENT OF FEES\t       |")
        print("------------------------------------------------")
        print(f"| TUITION FEE LECTURE \t\t: {self.tuition_fee_lecture:<{width}.2f} |")
        print(f"| AdU CHRONICAL \t\t: {self.adu_chronical:<{width}.2f} |")
        print(f"| ATHLETIC     \t\t\t: {self.athletic:<{width}.2f} |")
        print(f"| AUDIO-VISUAL LIBRARY \t\t: {self.audio_visual_library:<{width}.2f} |")
        print(f"| AUSG     \t\t\t: {self.ausg:<{width}.2f} |")
        print(f"| CULTURAL FEE \t\t\t: {self.cultural_fee:<{width}.2f} |")
        print(f"| ENERGY COST, AIRCON CLASSROOM : {self.energy_cost:<{width}.2f} |")
        print(f"| GUIDANCE     \t\t\t: {self.guidance:<{width}.2f} |")
        print(f"| INSURANCE FEE \t\t: {self.insurance_fee:<{width}.2f} |")
        print(f"| LEARNING MANAGEMENT SYSTEM    : {self.learning_management_system:<{width}.2f} |")
        print(f"| LIBRARY FEE \t\t\t: {self.library_fee:<{width}.2f} |")
        print(f"| MEDICAL AND DENTAL \t\t: {self.medical_dental:<{width}.2f} |")
        print(f"| REGISTRATION \t\t\t: {self.registration:<{width}.2f} |")
        print(f"| RSO \t\t\t\t: {self.rso:<{width}.2f} |")
        print(f"| STUDENT ACTIVITIES FEE \t: {self.student_activities:<{width}.2f} |")
        print(f"| STUDENT NURTURANCE FEE \t: {self.student_nurturance:<{width}.2f} |")
        print(f"| TECHNOLOGY FEE \t\t: {self.technology_fee:<{width}.2f} |")
        print(f"| TEST PAPERS     \t\t: {self.test_papers:<{width}.2f} |")
        print(f"| Assessment Amount \t\t: {self.other_assessment:<{width}.2f} |")
        print(f"| Downpayment \t\t\t: {self.downpayment:<{width}.2f} |")
        print(f"| Total Due \t\t\t: {self.total_due:<{width}.2f} |")
        print("-" * 48)
        print(f"| PRELIM     \t\t\t: {self.prelim:<{width}.2f} |")
        print(f"| MIDTERM     \t\t\t: {self.midterm:<{width}.2f} |")
        print(f"| FINAL     \t\t\t: {self.final:<{width}.2f} |")
        print("-" * 48)
