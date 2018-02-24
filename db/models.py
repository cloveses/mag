# import pony.orm
from .mypony import pony
from pony.orm import Required

db = pony.db

class Person(db.Entity):
    name = Required(str, 50)
    age = Required(int)
      