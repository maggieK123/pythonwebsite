
from flask import Blueprint, render_template, request, flash, jsonify

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("basic.html")



@views.route('/test')
def test():
    return render_template("test.html")

