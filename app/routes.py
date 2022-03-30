
from app import app
from flask import render_template
from app.forms import RegisterPhoneForm


@app.route('/')
def index():
    title="Home"
    return render_template('index.html', title=title)

@app.route('/register_phone', methods=["GET", "POST"])
def phone(): 
    title = 'Register phone'
    form = RegisterPhoneForm()
    return render_template('register_phone.html', title=title, form=form)
    
