from selenium import webdriver

from fixtures.group import GroupHelper
from fixtures.contact import ContactHelper
from fixtures.session import Session


class Application:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        # self.driver.implicitly_wait(1)
        self.session = Session(self)
        self.groupHelper = GroupHelper(self)
        self.contactHelper = ContactHelper(self)

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
