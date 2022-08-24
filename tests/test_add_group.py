from models.group import Group


def test_add_group(app):
    old_groups = app.groupHelper.get_group_list()
    app.groupHelper.add_new_group(Group(name="test1"))
    new_groups = app.groupHelper.get_group_list()

    assert len(new_groups) - 1 == len(old_groups)
