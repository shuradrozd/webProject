from selenium import webdriver
from selenium.webdriver.common.by import By

from fixtures.group import Group
from fixtures.session import Session


class Application:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.session = Session(self)
        self.group = Group(self)

    def open_home_page(self):
        self.driver.get("http://localhost/addressbook/")

    def destroy(self):
        self.driver.quit()