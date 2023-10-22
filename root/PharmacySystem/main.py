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

class Medication:
    def __init__(self, MedicationId, MedicationName, Description, Dosage, Price, Manufacturer, ExpirationDate):
        self.MedicationId = MedicationId
        self.MedicationName = MedicationName
        self.Description = Description
        self.Dosage = Dosage
        self.Price = Price
        self.Manufacturer = Manufacturer
        self.ExpirationDate = ExpirationDate 

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
    def __init__(self, OrderId, Customer, Medication, TotalPrice):
        self.OrderId = OrderId
        self.Customer = Customer
        self.Medication = Medication
        self.TotalPrice = TotalPrice
