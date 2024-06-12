
def render_user_list(users):
   return [
      {
         "id": user.id,
         "name": user.name,
         "email": user.email,
         "password": user.password,
         "phone": user.phone,
         "role": user.role,
      }
      for user in users
   ]

def render_user_detail(user):
   return [
      {
         "id": user.id,
         "name": user.name,
         "email": user.email,
         "password": user.password,
         "phone": user.phone,
         "role": user.role,
      }
   ]
