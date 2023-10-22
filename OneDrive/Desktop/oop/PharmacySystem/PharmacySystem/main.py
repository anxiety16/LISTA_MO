class Pharmacy:
    def __init__(self, PharmacyId, PharmacyName, PharmacyLocation):
        self.PharmacyId = PharmacyId
        self.PharmacyName = PharmacyName
        self.PharmacyLocation = PharmacyLocation

class Customer:
    def __init__(self, CustomerId, CustomerName, CustomerAddress, ContactNumber):
        self.CustomerId = CustomerId
        self.CustomerName = CustomerName
        self.CustomerAddress = CustomerAddress
        self.ContactNumber = ContactNumber

    def PlaceOrder(self):
        print(f'Order Placed by {self.CustomerName} with Prescription ID: {self.PrescriptionId}')

    def ViewRecentOrder(self):

class Medication:
    def __init__(self, NameId, Description, Dosage, Price, Manufacturer, ExpirationDate):
        self.NameId = NameId
        self.Description = Description
        self.Dosage = Dosage
        self.Price = Price
        self.Manufacturer = Manufacturer
        self.ExpirationDate = ExpirationDate

    def DistributeMeds(self):

    def CheckStocks(self):

class Pharmacist:
    def __init__(self, PharmacistId, PharmacistName, LicenseNumber):
        self.PharmacistId = PharmacistId
        self.PharmacistName = PharmacistName
        self.LicenseNumber = LicenseNumber

    def FillPrescription(self):

    def ManageInventory(self):

class Prescription(Customer, Pharmacist, Medication):
    def __init__(self,CustomerName, PharmacistName, NameId, Dosage, PrescriptionId, DateIssued, DateFilled):
        super().__init__(CustomerName, PharmacistName, NameId, Dosage)
        self.PrescriptionId = PrescriptionId
        self.DateIssued = DateIssued
        self.DateFilled = DateFilled

    def AddMeds(self):

    def RemoveMeds(self):

class Inventory(Medication):
    def __init__(self,QuantityStock):
        super().__init__()
        self.QuantityStock = QuantityStock

    def UpdateStocks(self):

    def CheckExpirationDate(self):