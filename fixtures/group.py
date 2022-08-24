from selenium.webdriver.common.by import By

from models.group import Group


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def add_new_group(self, group):
        driver = self.app.driver
        self.open_group_page()
        driver.find_element(By.NAME, "new").click()
        driver.find_element(By.NAME, "group_name").click()
        driver.find_element(By.NAME, "group_name").send_keys(group.name)
        driver.find_element(By.NAME, "submit").click()
        self.open_group_page()

    def open_group_page(self):
        driver = self.app.driver
        if driver.current_url.endswith("/group.php"):
            if len(driver.find_elements(By.NAME, "new")) > 0:
                return
        driver.find_element(By.LINK_TEXT, "groups").click()

    def delete_first_group(self):
        driver = self.app.driver
        self.open_group_page()
        driver.find_element(By.XPATH, "//span[1]/input").click()
        driver.find_element(By.NAME, "delete").click()
        self.open_group_page()

    def modify_first_group(self, group):
        driver = self.app.driver
        self.open_group_page()
        if group.name is not None:
            driver.find_element(By.XPATH, "//span[1]/input").click()
            driver.find_element(By.XPATH, "(//input[@name='edit'])[1]").click()
            driver.find_element(By.NAME, "group_name").click()
            driver.find_element(By.NAME, "group_name").clear()
            driver.find_element(By.NAME, "group_name").send_keys(group.name)
            driver.find_element(By.NAME, "update").click()
            self.open_group_page()

    def count(self):
        driver = self.app.driver
        self.open_group_page()
        return len(driver.find_elements(By.XPATH, "//input[@type='checkbox']"))

    def get_group_list(self):
        driver = self.app.driver
        self.open_group_page()
        groups = []
        for element in driver.find_elements(By.XPATH, "//span[@class='group']"):
            text = element.text
            ident = element.find_element(By.NAME, 'selected[]').get_attribute("value")
            groups.append(Group(name=text, id=ident))
        return groups
