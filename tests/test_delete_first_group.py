from models.group import Group


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.add_new_group(Group(name="hello"))
    app.group.delete_first_group()
