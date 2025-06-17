from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import MetaData

metadata = MetaData()
db = SQLAlchemy(metadata=metadata)

class Student(db.Model):
    __tablename__ = 'students'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    
    cohort_id = db.Column(db.Integer, db.ForeignKey('cohorts.id'), nullable=False)
    cohort = db.relationship("Cohort", back_populates='students')

    # def __repr__(self):
    #     return f"<Student id={self.id} name='{self.name}' cohort_id={self.cohort_id}>"

class Mentor(db.Model):
    __tablename__ = 'mentors'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    cohorts = db.relationship("Cohort", back_populates='mentor')
    rewards = db.relationship("Reward", back_populates='mentor')

class Cohort(db.Model):
    __tablename__ = 'cohorts'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)

    mentor_id = db.Column(db.Integer, db.ForeignKey("mentors.id"))
    mentor = db.relationship('Mentor', back_populates='cohorts')

    students = db.relationship('Student', back_populates='cohort')

class Reward(db.Model):
    __tablename__ = 'rewards'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    mentor_id = db.Column(db.Integer, db.ForeignKey('mentors.id'))
    mentor = db.relationship('Mentor', back_populates='rewards')
