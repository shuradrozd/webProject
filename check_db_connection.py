from fixtures.orm import ORMFixture

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
try:
    gr = db.get_contact_list()
    for group in gr:
        print(group)
finally:
    pass
