#from student import Student
from datetime import datetime
curr_year = datetime.now().year

class Student:
    def __init__(self, nm,em,pn):
        self.name = nm
        self.email = em
        self.phone_number = pn


    def set_data(self):
        print("can you please enter your data")
        self.name = (input("name: ").strip()).title()
        self.email = input("email: ").strip()
        self.phone_number = int(input("phone number: "))
    
    def get_data(self):
        return self.name,self.email,self.phone_number

    @property
    def get_name(self):
        return self.name

    @property
    def get_email(self):
        return self.email

    @property
    def get_phone_number(self):
        return self.phone_number

    def set_name(self, nm):
        self.name = nm

    def set_email(self, em):
        self.email = em

    def set_phone_number(self, num):
        self.phone_number = num

    def __str__(self):
        return f"{self.name}\t{self.email}\t{self.phone_number}"


class applying_student(Student):


    def __init__(self,nm,em,pn,address,school):
        super().__init__(nm,em,pn)
        self.address = address
        self.school = school
        self.set_id()

    applied_counter = int(f"{str(curr_year)[2:]}00000")
    applied_students = []
    
    @property
    def set_address(self,adress):
        self.address = adress
    
    @property
    def get_address(self):
        return self.address
    
    @property
    def set_school(self,school):
        self.school = school
    
    def get_school(self):
        return self.school
    
    def set_id(self):
        self.id = f"CU{applying_student.applied_counter}"
        applying_student.applied_counter +=1

    @property
    def get_id(self):
        return self.id 
    
    def apply(self, name, email, phone,address,school):
        self.set_id()
        self.set_name(name)
        self.set_address(address)
        self.set_school(school)
        self.set_email(email)
        self.set_phone_number(phone)
        applying_student.applied_students.append(self)

