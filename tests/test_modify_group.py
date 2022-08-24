from models.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.add_new_group(Group(name="hello"))
    app.group.modify_first_group(Group(name="New group"))
