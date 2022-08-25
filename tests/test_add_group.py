import random
import string

import pytest

from models.group import Group


def random_string(prefix, maxLen):
    symbols = string.ascii_letters + string.digits + " " * 2
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxLen))])


test_data = [Group(name="")] + [Group(name=random_string("name", 10))
                                for i in range(5)
                                ]


@pytest.mark.parametrize("group", test_data, ids=[repr(x) for x in test_data])
def test_add_group(app, group):
    old_groups = app.groupHelper.get_group_list()
    app.groupHelper.add_new_group(group)

    assert len(old_groups) + 1 == app.groupHelper.count()
    new_groups = app.groupHelper.get_group_list()
    old_groups.append(group)

    assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)
