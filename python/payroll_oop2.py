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

    def diplay_data(self):
        print("Company Name: ", self.company_name)
        print("Employee Department: ", self.emp_department)
        print("Employee Name: ", self.emp_name)
        print("Employee Code: ", self.emp_code)
        print("")
