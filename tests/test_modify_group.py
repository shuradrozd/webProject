from models.group import Group


def test_modify_group_name(app):
    if app.groupHelper.count() == 0:
        app.groupHelper.add_new_group(Group(name="hello"))
    old_groups = app.groupHelper.get_group_list()
    group = Group(name="New group")
    group.id = old_groups[0].id

    app.groupHelper.modify_first_group(group)
    new_groups = app.groupHelper.get_group_list()

    assert len(new_groups) == len(old_groups)
    old_groups[0] = group

    assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)
