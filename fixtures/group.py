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
        self.group_cache = None

    def open_group_page(self):
        driver = self.app.driver
        if driver.current_url.endswith("/group.php"):
            if len(driver.find_elements(By.NAME, "new")) > 0:
                return
        driver.find_element(By.LINK_TEXT, "groups").click()

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        driver = self.app.driver
        self.open_group_page()
        elem = "//span[{}]/input".format(index + 1)
        driver.find_element(By.XPATH, elem).click()
        driver.find_element(By.NAME, "delete").click()
        self.open_group_page()
        self.group_cache = None

    def delete_group_by_id(self, id):
        driver = self.app.driver
        self.open_group_page()
        self.select_group_by_id(id)
        # elem = "//span[{}]/input".format(id)
        # driver.find_element(By.XPATH, elem).click()
        driver.find_element(By.NAME, "delete").click()
        self.open_group_page()
        self.group_cache = None

    def select_group_by_id(self, id):
        driver = self.app.driver
        driver.find_element(By.CSS_SELECTOR, "input[value='%s']" % id).click()

    def modify_first_group(self, group):
        self.modify_group_by_index(group, 0)

    def modify_group_by_index(self, group, index):
        driver = self.app.driver
        self.open_group_page()
        if group.name is not None:
            elem = "//span[{}]/input".format(index + 1)
            driver.find_element(By.XPATH, elem).click()
            driver.find_element(By.XPATH, "(//input[@name='edit'])[1]").click()
            driver.find_element(By.NAME, "group_name").click()
            driver.find_element(By.NAME, "group_name").clear()
            driver.find_element(By.NAME, "group_name").send_keys(group.name)
            driver.find_element(By.NAME, "update").click()
            self.open_group_page()
        self.group_cache = None

    def count(self):
        driver = self.app.driver
        self.open_group_page()
        return len(driver.find_elements(By.XPATH, "//input[@type='checkbox']"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            driver = self.app.driver
            self.open_group_page()
            self.group_cache = []
            for element in driver.find_elements(By.XPATH, "//span[@class='group']"):
                text = element.text
                ident = element.find_element(By.NAME, 'selected[]').get_attribute("value")
                self.group_cache.append(Group(name=text, id=ident))
        return list(self.group_cache)
