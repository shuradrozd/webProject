from selenium import webdriver

from fixtures.group import Group
from fixtures.session import Session


class Application:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.session = Session(self)
        self.group = Group(self)

    def is_valid(self):
        try:
            self.driver.current_url
            return True
        except:
            return False

    def open_home_page(self):
        self.driver.get("http://localhost/addressbook/")

    def destroy(self):
        self.driver.quit()
