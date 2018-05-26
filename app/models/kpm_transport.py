from app import db


class KPMTruck(db.Model):
    __tablename__ = "kpm_trucks"
    id = db.Column(db.Integer(), primary_key=True)
    model = db.Column(db.String(), nullable=False)


class KPMEmployee(db.Model):
    __tablename__ = "kpm_employees"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
