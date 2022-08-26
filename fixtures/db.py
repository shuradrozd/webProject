import mysql.connector

from models.group import Group


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)

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

    def destroy(self):
        self.connection.close()
