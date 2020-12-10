import pickle
from Admin import Admin
try:
    dbfile = open("database", "rb")
    database = pickle.load(dbfile)
    dbfile.close()
except FileNotFoundError:
    database = {"user_confirmed": {}, "user_waiting": {}, "appointment": {}, "all_availability": {}}
    new_admin = Admin("admin", "111", "admin", "title", "firstName", "lastName", "birthDate", "gender", "telephone",
                 "address")
    database["user_confirmed"]["admin"] = new_admin