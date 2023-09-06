from app import db
from app.Model.models import Student, Class, Major, enrolled
#create the database file, if it doesn't exist. 
db.create_all()

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
from app.Model.models import Class
newClass = Class(coursenum='322',major='CptS',title='Software Engineering')
db.session.add(newClass)
newClass = Class(coursenum='315',major='CE',title='Fluid Mechanics')
db.session.add(newClass)
db.session.commit()


allClasses = Class.query.all()
Class.query.filter_by(major='CptS').all()
Class.query.filter_by(major='CptS').first()
Class.query.filter_by(major='CptS').order_by(Class.title).all()
Class.query.filter_by(major='CptS').count()
mymajor = Major.query.filter_by(name='CptS').first()
for c in mymajor.classes:
    print(c.title)
