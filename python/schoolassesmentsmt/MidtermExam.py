class ServiceInformation:
    def __init__(self):
        self.contract_number = ""
        self.account_name = ""
        self.service_address = ""
        self.tin_number = ""
        self.rate_class = ""
        self.bussiness_area = ""

    def get_service_information(self, contract_number, account_name, service_address, tin_number, rate_class, bussines_area):
        self.contract_number = contract_number
        self.account_name = account_name
        self.service_address = service_address
        self.tin_number = tin_number
        self.rate_class = rate_class 
        self.bussiness_area = bussines_area

    def displayServiceInformation(self):
        print('\tAdvisory \t: Check payment WILL NOT BE ACCEPTED without the')
        print('\tStatement of Account effective October 01, 2019')
        print('--------------------------------------------------------------------')
        print('\t\t\t\t\t\t\t\t\tMaynilad Water Services, Inc.')
        print('\t\t\t\t\t\t\t\t\t8390 DR A SANTOS AVE BF HOMES')
        print('\t\t\t\t\t\t\t\t\tPARANAQUE CITY')
        print('\t\t\t\t\t\t\t\t\tVAT Reg TIN 005-393-442-0000')
        print('\t\t\t\t\t\t\t\t\tSPM No.:')
        print('\t\t\t\t\t\t\t\t\tMachine SN:')
        print('')
        print('SOA \t#\t 00000000003456789012')
        print('\t\t  Statement of Account\t')
        print('\tFor the month of: February 2024\t')
        print('\t\t  SERVICE INFORMATION\t')
        print('')
        print(f"Contract Account No\t: {self.contract_number}")
        print(f"Account Name\t: {self.account_name}")
        print(f"Service Address\t: {self.service_address}")
        print(f"TIN\t\t\t\t: {self.tin_number}")
        print(f"Rate Class\t\t: {self.rate_class}")
        print(f"Business Area\t: {self.bussiness_area}")
        print('--------------------------------------------------------------------')

class MeteringInformation:
    def __init__(self):
        self.meter_number = ""
        self.mru_nu = 0.00
        self.seq_num = ""
        self.reading_date = ""
        self.present_reading = 0.00
        self.previous_reading = 0.00
        self.consumption = 0.00

    def get_metering_information(self, meter_number, mru_nu, seq_num, reading_date, present_reading, previous_reading, consumption):
        self.meter_number = meter_number
        self.mru_nu = mru_nu
        self.seq_num = seq_num
        self.reading_date = reading_date
        self.present_reading = present_reading
        self.previous_reading = previous_reading
        self.consumption = consumption

    def displayMeteringInformation(self):
        print('\t\t\t\t\t\tMETERING INFORMATION\t\t\t\t\t\t')
        print('Meter No. \t\t\t\t\t MRU NO. \t\t\t\t\t Seq No.')
        print(f'{self.meter_number} \t\t\t {self.mru_nu} \t\t\t\t\t {self.seq_num}')
        print(f'Reading Date\t\t: {self.reading_date}')
        print(f'Present Reading\t\t: {self.present_reading}')
        print(f'Previous Reading\t: {self.previous_reading}')
        print(f'Consumption (cu.m)  : {self.consumption}')
        print('Previous 3 Months Consumption')
        print('--------------------------------------------------------------------')
        print('\t\t\t\t\t\t BILL & PAYMENT HISTORY \t\t\t\t\t\t\t\t')
        print('Desc \t\t Total Amount \t\t\tOR# \t\t\t Date')
        print('')
        print('Description: WB-Water Bill, GD-Guarantee Deposit, MISC-Reopening Fee,')
        print('Connection Fee, Metering Charge')
        print('--------------------------------------------------------------------')

class BillingSummary:
    def __init__(self):
        self.billing_period = ""
        self.consump = 0.00
        self.current_charges = 0.00
        self.basic_charge = 0.00
        self.environmental_charges = 0.00
        self.maintenance_charges = 0.00
        self.charges_before_taxes = 0.00
        self.government_taxes = 0.00
        self.total_amount_due = 0.00
        self.payment_due_date = ""

    def consumption(self, consumption, paymentduedate, maintenance_charges):
        self.consump = consumption
        self.payment_due_date = paymentduedate
        self.maintenance_charges = maintenance_charges

        self.basic_charge = consumption * 23.52
        self.environmental_charges = (self.basic_charge * 0.20)
        self.charges_before_taxes = self.basic_charge + self.environmental_charges + self.maintenance_charges
        self.government_taxes = self.charges_before_taxes * 0.025
        self.total_amount_due = self.charges_before_taxes + self.government_taxes
        self.current_charges = self.charges_before_taxes + self.government_taxes

    def display_billing_summary(self):
        width = 61
        width2 = 53
        width3 = 57
        width4 = 57
        print('\t\t\t\t\t\t  BILLING SUMMARY  \t\t\t\t\t\t')
        print('BILLING PERIOD\t: 01/24/2024 TO 02/23/2024')
        print(f'{'Current Charges':{width}} {self.current_charges:.2f}')
        print(f'{'Environmental Service Charge (20% of Basic Charge)':{width}} {self.environmental_charges:.2f}')
        print(f'{'Maintenance Service Charge (MSC)':{width}}   {self.maintenance_charges:.2f}')
        print(f'{'Total Current Charges Before Taxes':{width}} {self.charges_before_taxes:.2f}')
        print(f'{'Government Taxes':{width}}  {self.government_taxes:.2f}')
        print('--------------------------------------------------------------------')
        print(f'{'TOTAL AMOUNT DUE':{width3}} PHP {self.total_amount_due:.2f}')
        print(f'{'PAYMENT DUE DATE':{width4}} {self.payment_due_date}')
        print('--------------------------------------------------------------------')
