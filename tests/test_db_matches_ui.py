from models.group import Group


def test_group_list(app, db):
    ui_groups = app.groupHelper.get_group_list()

    def clean(group):
        return Group(name=group.name.strip(), id=group.id)

    db_groups = map(clean, db.get_group_list())

    assert sorted(ui_groups, key=Group.id_or_max) == sorted(db_groups, key=Group.id_or_max)
