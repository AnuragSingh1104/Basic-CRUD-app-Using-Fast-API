from sqlalchemy.orm import Session
import models,schemas

def get_employee(db:Session):
    return db.query(models.Employee).all()



def get_employee_by_id(db:Session,employee_id:int):
    return (
        db.query(models.Employee)
        .filter(models.Employee.id==employee_id)
        .first()
    )



def create_employee(db:Session,employee:schemas.EmployeeCreate):
    db_emp=models.Employee(
        name=employee.name,
        email=employee.email,
        phone_number=employee.phone_number,
    )

    db.add(db_emp)
    db.commit()
    db.refresh(db_emp)
    return db_emp


def update_employee(db:Session,employee_id:int,employee:schemas.EmployeeUpdate):
    db_emp=(
        db.query(models.Employee)
        .filter(models.Employee.id==employee_id)
        .first()
    )

    if db_emp:
        db_emp.name=employee.name # type: ignore
        db_emp.email=employee.email # type: ignore
        db_emp.phone_number=employee.phone_number # type: ignore

        db.commit()
        db.refresh(db_emp)
        return db_emp
    
    else:
        return None
    

def delete_employee(db:Session,employee_id:int):
    db_emp=(
        db.query(models.Employee)
        .filter(models.Employee.id==employee_id)
        .first())
    
    if db_emp:
        db.delete(db_emp)
        db.commit()
    return db_emp