

from app import db
#create the database file, if it doesn't exist. 
db.create_all()

#import Major model
from app.models import Major

# Create a major
newMajor = Major(name='CptS',department='school of EECS')
db.session.add(newMajor)
newMajor = Major(name='CE',department='Civil Engineering')
db.session.add(newMajor)
db.session.commit()
Major.query.all()
for m in Major.query.all():
    print(m)

#Create a class; assign class's major to the major we just created
from app.models import Class
NewClass = Class(coursenum='322',major='CptS',title='Software Engineering')
db.session.add(newClass)
NewClass = Class(coursenum='315',major='CE',title='Fluid Mechanics')
db.session.add(newClass)


# import db models
from app.models import Class

#create class objects and write them to the database
newClass = Class(coursenum='322')
db.session.add(newClass)
newClass = Class(coursenum='355')
db.session.add(newClass)
db.session.commit()

# query and print classes
Class.query.all()
Class.query.filter_by(coursenum='322').all()
Class.query.filter_by(coursenum='322').first()
myclasses = Class.query.order_by(Class.coursenum.desc()).all()
for c in myclasses:
    print(c.coursenum)
