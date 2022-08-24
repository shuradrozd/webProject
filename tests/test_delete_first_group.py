from models.group import Group


def test_delete_first_group(app):
    if app.groupHelper.count() == 0:
        app.groupHelper.add_new_group(Group(name="hello"))
    old_groups = app.groupHelper.get_group_list()
    app.groupHelper.delete_first_group()
    new_groups = app.groupHelper.get_group_list()

    assert len(old_groups) - 1 == len(new_groups)
