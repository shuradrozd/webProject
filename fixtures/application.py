from selenium import webdriver
from selenium.webdriver.common.by import By

from fixtures.session import Session


class Application:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.session = Session(self)

    def add_new_group(self, group):
        self.driver.find_element(By.LINK_TEXT, "groups").click()
        self.driver.find_element(By.NAME, "new").click()
        self.driver.find_element(By.NAME, "group_name").click()
        self.driver.find_element(By.NAME, "group_name").send_keys(group.name)
        self.driver.find_element(By.NAME, "submit").click()
        self.driver.find_element(By.LINK_TEXT, "groups").click()

    def open_home_page(self):
        self.driver.get("http://localhost/addressbook/")

    def destroy(self):
        self.driver.quit()