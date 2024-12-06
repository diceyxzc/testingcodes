import MidtermExam

class GetServiceInfo:

    def input_service_information(self):
        obj = MidtermExam.ServiceInformation()
        print("---Service Information---")
        contract_number = int(input("Enter Contract Number: "))
        account_name = input("Enter Account Name: ")
        service_address = input("Enter Service Address: ")
        tin_number = input("TIN Number: ")
        rate_class = input("Rate Class: ")
        bussiness_area = input("Business Area: ")

        obj2 = MidtermExam.MeteringInformation()
        print("---Metering Information")
        meter_number = input("Meter Number: ")
        mru_num = int(input("MRU No.: "))
        seq_num = input("Sequence Number: ")
        reading_date = input("Reading Date: ")
        present_reading = int(input("Present Reading: "))
        previous_reading = int(input("Previous Reading: "))
        consumption = int(input("Consumption: "))

        obj3 = MidtermExam.BillingSummary()
        print("---Billing Summary---")
        maintenance_charges = float(input("Maintenance Charge: "))
        payment_due_date = input("Payment Due Date: ")

        service_information = obj.get_service_information(contract_number, account_name, service_address, tin_number,
                                                          rate_class, bussiness_area)

        metering_information = obj2.get_metering_information(meter_number, mru_num, seq_num, reading_date,
                                                             present_reading, previous_reading, consumption)

        consump = obj3.consumption(consumption, payment_due_date, maintenance_charges)

        obj.displayServiceInformation()
        obj2.displayMeteringInformation()
        obj3.display_billing_summary()

a = GetServiceInfo()
a.input_service_information()
