from models.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.add_new_group(Group(name="test1"))
    app.session.logout()
