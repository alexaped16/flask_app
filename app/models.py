from app import db
from datetime import datetime
#from werkzeug.security import generate_password_hash, check_password_hash

class PhoneBook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(10), unique=True, nullable=False)
    address = db.Column(db.String(100), unique=True, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #self.password = generate_password_hash(kwargs['password'])

    def __repr__(self): 
        return f"<User|{self.first_name}>"

    #def check_password(self, password):
        #return check_password_hash(self.password, password)