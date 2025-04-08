class patient(object):
    def __init__(self,name,age,admission_date,medical_history):
        self.name=name
        self.age=age
        self.admission_date=admission_date
        self.medical_history=medical_history
        print(f"{self.name}, Age: {self.age}, Last Admission: {self.admission_date}, History: {self.medical_history}")
patient1=patient("Amy Green",18,"2025.4.8","heart attack")