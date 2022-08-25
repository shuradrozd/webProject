from selenium import webdriver

from fixtures.contact import ContactHelper
from fixtures.group import GroupHelper
from fixtures.session import Session


class Application:
    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.driver = webdriver.Firefox()
        elif browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "edge":
            self.driver = webdriver.Edge()
        else:
            raise ValueError("Unrecognized browser %" % browser)
        self.driver.maximize_window()
        # self.driver.implicitly_wait(2)
        self.session = Session(self)
        self.groupHelper = GroupHelper(self)
        self.contactHelper = ContactHelper(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.driver.current_url
            return True
        except:
            return False

    def open_home_page(self):
        self.driver.get(self.base_url)

    def destroy(self):
        self.driver.quit()
