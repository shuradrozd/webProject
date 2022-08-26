import random

from models.group import Group


def test_delete_some_group(app, db, check_ui):
    if app.groupHelper.count() == 0:
        app.groupHelper.add_new_group(Group(name="hello"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.groupHelper.delete_group_by_id(group.id)
    new_groups = db.get_group_list()

    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == app.groupHelper.get_group_list()


def test_delete_first_group(app, db, check_ui):
    if app.groupHelper.count() == 0:
        app.groupHelper.add_new_group(Group(name="hello"))
    old_groups = db.get_group_list()
    app.groupHelper.delete_first_group()
    new_groups = db.get_group_list()

    assert len(old_groups) - 1 == len(new_groups)
    old_groups[0:1] = []
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == app.groupHelper.get_group_list()
