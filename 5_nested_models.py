#nested models means , in pydantic using a model in another model as a field its called nested models
from pydantic import BaseModel

class Address(BaseModel):
  street:str
  city:str
  state:str

class Patient(BaseModel):
  name:str
  gender:str
  age:int
  address: Address  #nested model

addess_dict={'street':'123 main st','city':'New York','state':'NY'}

address1=Address(**addess_dict)

patient_dict={'name':'MKS','gender':'male','age':34,'address':address1}

patient1=Patient(**patient_dict)

print(patient1)
print(patient1.address.city)
