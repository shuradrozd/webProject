from selenium.webdriver.common.by import By


class Group:
    def __init__(self, app):
        self.app = app

    def add_new_group(self, group):
        driver = self.app.driver
        driver.find_element(By.LINK_TEXT, "groups").click()
        driver.find_element(By.NAME, "new").click()
        driver.find_element(By.NAME, "group_name").click()
        driver.find_element(By.NAME, "group_name").send_keys(group.name)
        driver.find_element(By.NAME, "submit").click()
        driver.find_element(By.LINK_TEXT, "groups").click()
