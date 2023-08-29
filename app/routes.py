from flask import render_template, flash, redirect, url_for, request
from app import app,db

from app.forms import ClassForm, RegistrationForm, LoginForm
from app.models import Class, Major, Student
from flask_login import login_user, current_user, logout_user, login_required
from datetime import datetime

@app.before_request
def initDB(*args, **kwargs):
    if app.got_first_request:
        db.create_all()
        if Major.query.count()==0:
            majors=[{'name':'CptS','department':'School of EECS'},
                    {'name':'SE','department':'School of EECS'},
                    {'name':'EE','department':'School of EECS'},
                    {'name':'ME','department':'Mechanical Engineering'},
                    {'name':'MATH','department':'Mathematics'}, ]
            for t in majors:
                db.session.add(Major(name=t['name'],department=t['department']))
            db.session.commit()

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
@login_required
def index():
    allclasses = Class.query.order_by(Class.major).all()
    return render_template('index.html', title="Course List", classes = allclasses)

@app.route('/createclass/', methods=['GET','POST'])
@login_required
def createclass():
    cform = ClassForm()
    if cform.validate_on_submit():
        newClass = Class(coursenum = cform.coursenum.data, title = cform.title.data, major = cform.major.data.name )
        db.session.add(newClass)
        db.session.commit()
        flash('Class"' + newClass.major + '-' + newClass.coursenum + '" is created')
        return redirect(url_for('index'))
    return render_template('create_class.html', form =cform)

@app.route('/register/', methods=['GET','POST'])
def registerclass():
    rform = RegistrationForm()
    if rform.validate_on_submit():
        student = Student(username= rform.username.data, email= rform.email.data, firstname= rform.firstname.data, lastname= rform.lastname.data, address= rform.address.data)
        student.set_password(rform.password.data)
        db.session.add(student)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('index'))
    return render_template('register.html', form =rform)

@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen= datetime.utcnow()
        db.session.add(current_user)
        db.session.commit()


@app.route('/login', methods =['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    lform =LoginForm()
    if lform.validate_on_submit():
        student = Student.query.filter_by(username= lform.username.data).first()
        #if login fails#
        if (student is None) or (student.check_password(lform.password.data)==False):
            flash('Invalid username or password.')
            return redirect(url_for('login'))
        login_user(student, remember = lform.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title ='Sign In', form = lform)

@app.route('/logout', methods =['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/display_profile', methods=['GET'])
def display_profile():
    return render_template('display_profile.html', title='Display Profile', student = current_user)