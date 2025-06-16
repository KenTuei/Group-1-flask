from random import randint, choice as rc
from faker import Faker 
from app import app
from models import db, Student, Mentor, Reward, Cohort

if __name__ == '__main__':
    
    with app.app_context():
        db.drop_all()
        db.create_all()

student1=Student(name="Ken")
student2=Student(name="Elvis")
student3=Student(name="Yelsin")


mentor1=Mentor(name="Aaron")
mentor2=Mentor(name="Dennis")
mentor3=Mentor(name="Rose")

reward1=Reward(name='Laptop', mentor_id=1)
reward2=Reward(name='Biro', mentor_id=2)
reward3=Reward(name='Tecno', mentor_id=3)

cohort1=Cohort(name='Remote11', student_id=1, mentor_id=1, year=2011)
cohort2=Cohort(name='Remote12', student_id=2, mentor_id=2, year=2012)
cohort3=Cohort(name='Remote13', student_id=3, mentor_id=3, year=2013)

db.session.add_all()
db.session.commit()








