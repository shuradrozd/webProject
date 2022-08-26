from fixtures.orm import ORMFixture
from models.group import Group

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
try:
    gr = db.get_contacts_not_in_group(Group(id="370"))
    for group in gr:
        print(group)
finally:
    pass
