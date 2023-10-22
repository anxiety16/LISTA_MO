class Customer:
    def __init__(self, CustomerId, CustomerName, CustomerAddress, ContactNumber):
        self.CustomerId = CustomerId
        self.CustomerName = CustomerName
        self.CustomerAddress =CustomerAddress
        self.ContactNumber = ContactNumber
        self.Prescription = []

#Create class for the remaining (Pharmacist, Medication, Inventory, Prescription, & Order)

class Pharmacist:
    def __init__(self, PharmacistId, PharmacistName, LicenseNumber):
        self.PharmacistId = PharmacistId
        self.PharmacistName = PharmacistName
        self.LicenseNumber = LicenseNumber

    def loggin(self):
        print(f'\nWelcome {self.PharmacistName}')

class Medication:
    def __init__(self, MedicationId, MedicationName, Dosage, Price):
        self.MedicationId = MedicationId
        self.MedicationName = MedicationName
        self.Dosage = Dosage
        self.Price = Price

    def GetPrice(self):
        return self.Price

class Inventory:
    def __init__(self,QuantityStock, MedicationId):
        self.QuantityStock = QuantityStock
        self.MedicationId = MedicationId

class Prescription:
    def __init__(self, PrescriptionId, Customer, Medication, DateIssued):
        self.PrescriptionId = PrescriptionId
        self.Customer = Customer
        self.Medication = Medication
        self.DateIssued = DateIssued

class Order:
    def __init__(self, OrderId, Customer, Medications):
        self.OrderId = OrderId
        self.Customer = Customer
        self.Medications = Medications
        self.TotalPrice = sum(Medication.GetPrice() for Medication in Medications)

#FOR LOGGING IN OF PHARMACIST ADMIN
user = input("Enter Pharmacist License Number: ")
if user == '0101':
    customers = []
    medications = []

    customer = int(input("Enter the number of customers: "))

    for i in range(customer):
        name = input("Customer Name: ")
        address = input("Customer Address: ")
        phone = input("Customer Contact Number: ")
        customers.append(Customer(len(customers) + 1, name, address, phone))

    meds = int(input("Enter the number of medications: "))
    for i in range(meds):
        name = input("Medication Name: ")
        dosage = int(input("Dosage: "))
        price = float(input("Medication Price: "))
        medications.append(Medication(len(medications) + 1, name, dosage, price))

    CustomerId = int(input("Enter customer ID for the prescription: "))
    MedicationId = int(input("Enter medication ID for the prescription: "))
    DateIssued = input("Enter prescription date: ")
    customer = next((c for c in customers if c.CustomerId == CustomerId), None)
    medication = next((m for m in medications if m.MedicationId == MedicationId), None)

    if customer and medication:
        prescription = Prescription(len(customer.Prescription) + 1, customer, medication, DateIssued)
        customer.Prescription.append(Prescription)
        print("Prescription created.")
    else:
        print("Invalid customer or medication ID.")

# Display prescriptions for a customer
    CustomerId = int(input("Enter customer ID to display prescriptions: "))
    customer = next((c for c in customers if c.CustomerId == CustomerId), None)

    if customer:
        print(f"Prescriptions for {customer.CustomerName}:")
        for Prescription in customer.Prescription:
            print(f"Prescription ID: {Prescription.PrescriptionId}, Medication: {Prescription.Medication.MedicationName}, Date: {Prescription.DateIssued}")
    else:
        print("Invalid customer ID.")