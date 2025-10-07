#exporting pydantic model obj as py dict or dict
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

#exporting as dict

temp=patient1.model_dump(include=['name','gender']) #include and exclude are there , also exclude_unset
print(temp)

print(type(temp))

#exporting as json
temp=patient1.model_dump_json()
print(temp)

print(type(temp))
