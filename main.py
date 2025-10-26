from fastapi import FastAPI,HTTPException,Depends
from sqlalchemy.orm import Session
from database import SessionLocal,engine,Base
import models,schemas,crud
from typing import List

Base.metadata.create_all(bind=engine)

app=FastAPI()

#Dependency with the database

def get_database():
    db=SessionLocal() #creating a database session (contain session maker object)
    try:
        yield db
    finally:
        db.close()


# our endpoints

@app.post("/employees/",response_model=schemas.EmployeeOutput)
def create_employee(
    employee:schemas.EmployeeCreate,
    db:Session=Depends(get_database)
):
    return crud.create_employee(db,employee)


@app.get("/employees_read/",response_model=List[schemas.EmployeeOutput])
def read_employees(db:Session=Depends(get_database)):
    return crud.get_employee(db)


@app.get("/employees/{employee_id}",response_model=schemas.EmployeeOutput)
def read_employee_byid(
    employee_id: int,
    db:Session=Depends(get_database)
):
    if not crud.get_employee_by_id(db,employee_id):
        raise HTTPException(status_code=404,detail="Employee not found")
    else:
        return crud.get_employee_by_id(db,employee_id)
    
@app.put("/employees/{employee_id}",response_model=schemas.EmployeeOutput)
def update_employee(
    employee_id: int,
    employee: schemas.EmployeeUpdate,
    db: Session = Depends(get_database)
):
    if not crud.get_employee_by_id(db, employee_id):
        raise HTTPException(status_code=404, detail="Employee not found")
    return crud.update_employee(db, employee_id, employee)


@app.delete("/employees/{employee_id}",response_model=schemas.EmployeeOutput)
def delete_employee(
    employee_id: int,
    db: Session = Depends(get_database)
):
    if not crud.get_employee_by_id(db, employee_id):
        raise HTTPException(status_code=404, detail="Employee not found")
    return crud.delete_employee(db, employee_id)