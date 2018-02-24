from pony.orm import *
from .models import Person

@db_session
def test():
    p1 = Person(name='Mary', age=23)