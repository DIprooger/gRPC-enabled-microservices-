from piccolo.table import Table
from piccolo.columns import Varchar, Integer
from piccolo_conf import DB


class User(Table, db=DB):
    name = Varchar()
    email = Varchar()
    age = Integer()
