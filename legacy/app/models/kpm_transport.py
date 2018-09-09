from app import db
from app.models.base_models import Employee, Truck


class KPMTruck(db.Model, Truck):
    __tablename__ = "kpm_trucks"


class KPMEmployee(db.Model, Employee):
    __tablename__ = "kpm_employees"
