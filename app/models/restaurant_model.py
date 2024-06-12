from database import db

class Restaurant(db.Model):
   __tablename__ = "restaurants"
   
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(100), nullable=False)
   address = db.Column(db.String(100), nullable=False)
   city = db.Column(db.String(100), nullable=False)
   phone = db.Column(db.String(100), nullable=False)
   description = db.Column(db.String(100), nullable=False)
   raiting = db.Column(db.Float, nullable=False)
   
   def __init__(self, name, address, city, phone, description, raiting):
      self.name = name
      self.address = address
      self.city = city
      self.phone = phone
      self.description = description
      self.raiting = raiting
   
   def save(self):
      db.session.add(self)
      db.session.commit()
   
   @staticmethod
   def get_all():
      return Restaurant.query.all()


   @staticmethod
   def get_by_id(id):
      return Restaurant.query.get(id)


   def update(self, name=name, address=address, city=city, phone=phone, description=description, raiting=raiting):
      if name is not None:
         self.name = name
      if address is not None:
         self.address = address
      if city is not None:
         self.city = city
      if phone is not None:
         self.phone = phone
      if raiting is not None:
         self.raiting = raiting
      db.session.commit()

   def delete(self):
      db.session.delete(self)
      db.session.commit()