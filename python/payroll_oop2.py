class Employee_Info:
    def __init__(self):
        self.company_name = ""
        self.emp_department = ""
        self.emp_name = ""
        self.emp_code = ""
        self.salary_cut_off = ""

    def get_emp_data(self, company_name, emp_department, emp_name, emp_code, salary_cut_off):
        self.company_name = company_name
        self.emp_department = emp_department
        self.emp_name = emp_name
        self.emp_code = emp_code
        self.salary_cut_off = salary_cut_off

    def display_data(self):
        print("Company Name: ", self.company_name)
        print("Employee Department: ", self.emp_department)
        print("Employee Name: ", self.emp_name)
        print("Employee Code: ", self.emp_code)
        print("Cut-Off Date: ", self.salary_cut_off)

class Employee_Salary:
    def get_basic_pay(self, emp_rate_per_hour, emp_num_of_hours_per_payday):
        self.basic_pay = emp_rate_per_hour * emp_num_of_hours_per_payday
        return self.basic_pay

    def get_absences_deduction(self, emp_rate_per_hour, emp_num_of_absences):
        self.emp_absences = emp_num_of_absences * emp_rate_per_hour
        return self.emp_absences

    def get_overtime_pay(self, emp_hour_overtime, emp_rate_per_hour):
        self.overtime_pay = emp_hour_overtime * emp_rate_per_hour
        return self.overtime_pay

    def get_tardiness_deduction(self, emp_rate_per_hour, tardiness_num_hours):
        self.get_tardiness_deduction = tardiness_num_hours * emp_rate_per_hour
        return self.get_tardiness_deduction