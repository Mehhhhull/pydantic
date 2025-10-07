from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator
from typing import List,Dict,Optional,Annotated

#field validator is checking custom details, like does it have @hdfc.com in the gmail or not? something like this

class Patient(BaseModel):
  name:str
  email:EmailStr
  age:int
  weight:float
  married:bool
  allergies:List[str]
  contact_details:Dict[str,str]

  @field_validator('email')
  @classmethod #field validator is a class method
  def email_validator(cls,value):

    valid_domains=['hdfc.com','icici.com']
    #abc@gmail.com
    domain_name=value.split('@')[-1] #gmail.com
    if domain_name not in valid_domains:
      raise ValueError('Invalid email domain')
    return value
  
@field_validator('name')
@classmethod
def transform_name(clas,value):
  return value.upper()

def insert_patient_data(patient: Patient):

  print(patient.name)
  print(patient.age)
  print('inserted')

def update_patient_data(patient: Patient):

  print(patient.name)
  print(patient.age)
  print('updated')

patient_info={'name':'MKS','email':'abc@hdfc.com','age':18,'weight':75.2, 'married':True, 'allergies':['pollen','dust'], 'contact_details':{'phone':'1234567890'}}
              
patient1=Patient(**patient_info) #validation

update_patient_data(patient1)