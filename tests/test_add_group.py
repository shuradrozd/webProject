import pytest

from data.add_group import test_data
from models.group import Group


@pytest.mark.parametrize("group", test_data, ids=[repr(x) for x in test_data])
def test_add_group(app, group):
    old_groups = app.groupHelper.get_group_list()
    app.groupHelper.add_new_group(group)

    assert len(old_groups) + 1 == app.groupHelper.count()
    new_groups = app.groupHelper.get_group_list()
    old_groups.append(group)

    assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)
