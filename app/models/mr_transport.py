from app import db


class MRTruck(db.Model):
    __tablename__ = "mr_trucks"
    id = db.Column(db.Integer(), primary_key=True)
    model = db.Column(db.String(), nullable=False)


class MREmployee(db.Model):
    __tablename__ = "mr_employees"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
