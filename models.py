from sqlalchemy import Column,Integer,String,PrimaryKeyConstraint
from database import Base


class Employee(Base):
    __tablename__="employees"

    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,index=True,default="xyz")
    email=Column(String,unique=True,index=True,default="xyz@example.com")
    phone_number=Column(Integer,unique=True,index=True,default=1234567890)



class Department(Base):
    __tablename__="department"

    id=Column(Integer,primary_key=True,index=True)
    department_name=Column(String,index=True,default="General")
    location=Column(String,index=True,default="Head Office")
    
