from random import randrange

from models.group import Group


def test_delete_some_group(app):
    if app.groupHelper.count() == 0:
        app.groupHelper.add_new_group(Group(name="hello"))
    old_groups = app.groupHelper.get_group_list()
    index = randrange(len(old_groups))
    app.groupHelper.delete_group_by_index(index)
    new_groups = app.groupHelper.get_group_list()

    assert len(old_groups) - 1 == len(new_groups)
    old_groups[index:index + 1] = []
    assert old_groups == new_groups


def test_delete_first_group(app):
    if app.groupHelper.count() == 0:
        app.groupHelper.add_new_group(Group(name="hello"))
    old_groups = app.groupHelper.get_group_list()
    app.groupHelper.delete_first_group()
    new_groups = app.groupHelper.get_group_list()

    assert len(old_groups) - 1 == len(new_groups)
    old_groups[0:1] = []
    assert old_groups == new_groups
