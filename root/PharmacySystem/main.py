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


class Inventory:
    def __init__(self,QuantityStock, MedicationId):
        self.QuantityStock = QuantityStock
        self.MedicationId = MedicationId

class Prescription:


class Order:

