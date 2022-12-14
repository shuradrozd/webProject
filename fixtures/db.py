import mysql.connector

from models.contact import Contact
from models.group import Group


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit = True

    def get_group_list(self):
        groups = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name from group_list")
            for row in cursor:
                (id, name) = row
                groups.append(Group(name=name, id=str(id)))
        finally:
            cursor.close()
        return groups

    def get_contact_list(self):
        contacts = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname from addressbook")
            for row in cursor:
                (id, firstname, lastname) = row
                contacts.append(Contact(id=id, firstname=firstname, lastname=lastname))
        finally:
            cursor.close()
        return contacts

    def destroy(self):
        self.connection.close()
