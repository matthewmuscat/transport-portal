"""
The classes in this file are the base models
that define what goes in each user model.

All user models must inherit these classes.

This is to ensure that all user models are
implemented the same way. Failure to adhere
to this could lead to nasty, silent failures.
"""

from app import db


class Truck:
    __tablename__ = None
    id = db.Column(db.Integer(), primary_key=True)
    model = db.Column(db.String(), nullable=False)


class Employee:
    __tablename__ = None
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
