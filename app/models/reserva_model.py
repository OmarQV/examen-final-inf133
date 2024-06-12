from database import db

class Reserva(db.Model):
   __tablename__ = "reservas"
   
   id = db.Column(db.Integer, primary_key=True)
   user_id = db.Column(db.Integer, nullable= False)
   restaurant_id = db.Column(db.Integer, nullable=False)
   reservation_date = db.Column(db.DateTime, nullable=False)
   num_guests = db.Column(db.Integer, nullable=False)
   special_guests = db.Column(db.String(100), nullable=False)
   status = db.Column(db.String(100), nullable=False)
   
   def __init__(self, user_id, restaurant_id, reservation_date, num_guests, special_guests, status):
      self.user_id = user_id
      self.restaurant_id = restaurant_id
      self.reservation_date = reservation_date
      self.num_guests = num_guests
      self.special_guests = special_guests
      self.status = status
   
   def save(self):
      db.session.add(self)
      db.session.commit()
   
   @staticmethod
   def get_all():
      return Reserva.query.all()


   @staticmethod
   def get_by_id(id):
      return Reserva.query.get(id)


   def update(self, user_id, restaurant_id, reservation_date, num_guests, special_guests, status):
      if user_id is not None:
         self.user_id = user_id
      if restaurant_id is not None:
         self.restaurant_id = restaurant_id
      if reservation_date is not None:
         self.reservation_date = reservation_date
      if num_guests is not None:
         self.num_guests = num_guests
      if special_guests is not None:
         self.special_guests = special_guests
      if status is not None:
         self.status = status
      db.session.commit()

   def delete(self):
      db.session.delete(self)
      db.session.commit()
   