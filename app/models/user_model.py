from database import db
from werkzeug.security import generate_password_hash
import json
from flask_login import UserMixin


class User(db.Model, UserMixin):
   __tablename__ = "users"
   
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(100), nullable=False)
   email = db.Column(db.String(100), nullable=False)
   password = db.Column(db.String(100), nullable=False)
   phone = db.Column(db.String(100), nullable=False)
   role = db.Column(db.String(100), nullable=False)
   
   
   def __init__(self, name, email, password, phone, role=["customer"]):
      self.name = name
      self.email = email
      self.password = generate_password_hash(password)
      self.phone = phone
      self.role = json.dumps(role)
   
   def save(self):
      db.session.add(self)
      db.session.commit()
   
   @staticmethod
   def find_by_name(name):
      return User.query.filter_by(name=name).first()
   
   @staticmethod
   def get_all():
      return User.query.all()


   @staticmethod
   def get_by_id(id):
      return User.query.get(id)


   def update(self, name, email, password, phone, role=["customer"]):
      if name is not None:
         self.name = name
      if email is not None:
         self.email = email
      if password is not None:
         self.password = password
      if phone is not None:
         self.phone = phone
      if role is not None:
         self.role = role
      db.session.commit()

   def delete(self):
      db.session.delete(self)
      db.session.commit()