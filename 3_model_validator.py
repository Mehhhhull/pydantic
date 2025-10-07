from pydantic import BaseModel,EmailStr,AnyUrl,Field,model_validator
from typing import List,Dict,Optional,Annotated

#model validator is used to combine more than onefields and then do data validation

class Patient(BaseModel):
  name:str
  email:EmailStr
  age:int
  weight:float
  married:bool
  allergies:List[str]
  contact_details:Dict[str,str]

  @model_validator(mode='after') #after all the fields are validated then only this will run
  def validate_emergency_contact(cls,model):
    if model.age>60 and 'emergency' not in model.contact_details:
      raise ValueError('Emergency contact is required for patients above 60 years')
    return model

def insert_patient_data(patient: Patient):

  print(patient.name)
  print(patient.age)
  print('inserted')

def update_patient_data(patient: Patient):

  print(patient.name)
  print(patient.age)
  print('updated')

patient_info={'name':'MKS','email':'abc@hdfc.com','age':65,'weight':75.2, 'married':True, 'allergies':['pollen','dust'], 'contact_details':{'phone':'1234567890','emergency':'9876543210'}}
              
patient1=Patient(**patient_info) 

update_patient_data(patient1)