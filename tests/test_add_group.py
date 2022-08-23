import pytest

from fixtures.application import Application
from models.group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.add_new_group(Group(name="test1"))
    app.session.logout()
