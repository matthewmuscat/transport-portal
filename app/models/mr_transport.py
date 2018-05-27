from app import db
from app.models.base_models import Employee, Truck


class MRTruck(db.Model, Truck):
    __tablename__ = "mr_trucks"


class MREmployee(db.Model, Employee):
    __tablename__ = "mr_employees"
