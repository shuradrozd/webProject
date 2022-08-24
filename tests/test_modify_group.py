from models.group import Group


def test_modify_group_name(app):
    if app.groupHelper.count() == 0:
        app.groupHelper.add_new_group(Group(name="hello"))
    old_groups = app.groupHelper.get_group_list()
    app.groupHelper.modify_first_group(Group(name="New group"))
    new_groups = app.groupHelper.get_group_list()

    assert len(new_groups) == len(old_groups)
