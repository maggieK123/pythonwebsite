from flask import Blueprint,request,render_template,flash,redirect,url_for
from .models import User
from . import db
auth = Blueprint('auth', __name__)

@auth.route('/',methods = ['GET','POST'])
def basic():
    #login
    if request.method== 'POST' and request.form.get('name1') != None:
        name1 = request.form.get('name1')
        pass1 = request.form.get('password1')
        print(name1,pass1)
        user = User.query.filter_by(username = name1,password = pass1).first()
        if user:
            return redirect(url_for('views.test'))
        else:
            flash('wrong password')
            return redirect(url_for('views.home'))
#signup
    elif request.method =='POST':
        name2 = request.form.get('name2')
        pass2 = request.form.get('password2')
        
        
        #newuser = User(username = name2, password = pass2)
        #checks to see if user is in database
        user = User.query.filter_by(username = name2).first()
        if user:
            flash('User already exists, try again')
            return redirect(url_for('views.home'))

        newuser = User(username = name2, password = pass2)

        db.session.add(newuser)
        db.session.commit()
        print(name2,pass2)
        return redirect(url_for('views.test'))
    return render_template("basic.html") 