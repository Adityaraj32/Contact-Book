class contactBook:
    def __init__(self,personName,personPhoneNumber,personAddress):
        self.name = personName
        self.phonenumber = personPhoneNumber
        self.address = personAddress
    def printDetail(self):
        return f"Name is {self.name}\nPhone Number is {self.phonenumber}\nAddress is {self.address}"