from piccolo.table import Table
from piccolo.columns import Varchar, Integer, Text
from piccolo_conf import DB


class Order(Table, db=DB):
    user_id = Integer()
    title = Varchar()
    description = Text()


class User(Table, db=DB):
    name = Varchar()
    email = Varchar()
    age = Integer()
