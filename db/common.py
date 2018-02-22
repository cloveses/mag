# import pony.orm
import pony
from pony.orm import Required

db = pony.db

class Person(db.Entity):
    username = Required(str, 50)
    age = Required(int)




# db = pony.orm.Database()
# db.bind(provider='mysql',db='test')
# db.generate_mapping(create_tables=True)