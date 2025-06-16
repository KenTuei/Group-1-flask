from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import MetaData

metadata = MetaData()
db=SQLAlchemy(metadata=metadata)

class Student(db.Model):
    __tablename__='students'
    id= db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, nullable=False)

    cohort=db.relationship("Cohort", back_populates='students')


class Mentor(db.Model):
    __tablename__='mentors'
    id= db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, nullable=False)

    cohort=db.relationship("Cohort", back_populates='mentors')
    rewards=db.relationship("Reward", back_populates='mentors')




class Cohort(db.Model):
    __tablename__='cohorts'
    id= db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, nullable=False)
    students_id=db.Column(db.Integer, db.ForeignKey("students.id"))
    mentors_id=db.Column(db.Integer, db.ForeignKey("mentors.id"))
    year= db.Column(db.Integer , nullable=False)

class Reward(db.Model):
    __tablename__='rewards'
    id= db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, nullable=False)
    mentors_id=db.Column(db.Integer, db.ForeignKey("mentors.id"))

    mentor=db.relationship("Mentor", back_populates='rewards')











