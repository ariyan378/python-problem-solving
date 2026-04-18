class Patients:
    year = 2018
def __init__(self):
    self.age = 0
    self.weight = 0 #in Kg
    self.asthma = 0 #1 if yes
    
    
patient1 = Patients()
patient2 = Patients()
patient1.age, patient1.weight, patient1.asthma = 30, 60, 0
patient2.age, patient2.weight, patient2.asthma = 28, 55, 1
print(patient1.year)
patient1.year = 2019
print(patient1.year)
