from pydantic import BaseModel,EmailStr,AnyUrl,Field,computed_field
from typing import List,Dict,Optional,Annotated

# computed field, is a field whose value user doesnt provide,you create the value of this field using the other field values 

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float  # in kilograms
    height: float  # in meters
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    # ✅ Computed field must be INSIDE the class
    @computed_field(return_type=float)
    @property
    def calculate_bmi(self) -> float:
        bmi = self.weight / (self.height ** 2)
        return round(bmi, 2)

def insert_patient_data(patient: Patient):

  print(patient.name)
  print(patient.age)
  print('inserted')

def update_patient_data(patient: Patient):

  print(patient.name)
  print(patient.age)
  print(patient.calculate_bmi)
  print('updated')

patient_info={'name':'MKS','email':'abc@hdfc.com','age':65,'weight':75.2, 'height':'1.72', 'married':True, 'allergies':['pollen','dust'], 'contact_details':{'phone':'1234567890'}}
              
patient1=Patient(**patient_info) 

update_patient_data(patient1)