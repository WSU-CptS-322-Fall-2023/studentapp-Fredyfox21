from flask import Blueprint, render_template, flash, redirect, url_for
from app import app,db

from app.Controller.forms import RegistrationForm, LoginForm
from app.Model.models import Student
from flask_login import login_user, current_user, logout_user, login_required
from config import Config

routes_blueprint = Blueprint('auth', __name__)
routes_blueprint.template_folder = Config.TEMPLATE_FOLDER

@routes_blueprint.route('/registerclass/', methods=['GET','POST'])
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


@routes_blueprint.route('/login', methods =['GET','POST'])
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

@routes_blueprint.route('/logout', methods =['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))








