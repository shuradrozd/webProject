from models.group import Group


def test_add_group(app):
    app.group.add_new_group(Group(name="test1"))
