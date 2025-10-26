from pydantic import BaseModel,EmailStr
from typing import Optional

class EmployeeBase(BaseModel):
    name: str
    email: EmailStr
    phone_number: int



class EmployeeCreate(EmployeeBase):
    email: Optional[EmailStr]   #more specific so in inheritance it will override base class


class EmployeeUpdate(EmployeeBase):
    pass



class EmployeeOutput(EmployeeBase):
    id: int


    class Config:
        orm_mode = True