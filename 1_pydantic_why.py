from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict,Optional,Annotated

# making pydantic model and defining schema
class Patient(BaseModel):
# all the fields added is required by default
# to make optional , import option from typing module 
  name: Annotated[str,Field(max_length=50,title='Name of the patient',description='give the name of the patient in less than 50 words',example=['Mehul','SHubham'])]
  email:EmailStr #data validation 
  linkedin_url:AnyUrl
  age: int
  weight: Annotated[float,Field(gt=0,strict=True)]  #cant set value of weight more than 0, with strict true it onlky allows float to be sent
  married:bool =Annotated[bool,Field(default=None,description='is the patient married or not')] #setting default value   married:bool =False #setting default value
  allergies: Optional[List[str]]= None #here we make optional; also given default field when no one gives anything here
  contact_details:Dict[str,str]

def insert_patient_data(patient: Patient):

  print(patient.name)
  print(patient.age)
  print('inserted')

def update_patient_data(patient: Patient):

  print(patient.name)
  print(patient.age)
  print('updated')


patient_info={'name':'MKS','email':'abc@gmail.com','linkedin_url':'http://linkedin.com/1235','age':18,'weight':75.2, 'married':True, 'allergies':['pollen','dust'], 'contact_details':{'phone':'1234567890'}}

patient1=Patient(**patient_info)

update_patient_data(patient1)