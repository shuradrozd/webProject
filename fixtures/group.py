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

    def delete_first_group(self):
        driver = self.app.driver
        driver.find_element(By.LINK_TEXT, "groups").click()
        driver.find_element(By.XPATH, "//span[1]/input").click()
        driver.find_element(By.NAME, "delete").click()
        driver.find_element(By.LINK_TEXT, "groups").click()

    def modify_first_group(self, group):
        driver = self.app.driver
        driver.find_element(By.LINK_TEXT, "groups").click()
        if group.name is not None:
            driver.find_element(By.XPATH, "//span[1]/input").click()
            driver.find_element(By.XPATH, "(//input[@name='edit'])[1]").click()
            driver.find_element(By.NAME, "group_name").click()
            driver.find_element(By.NAME, "group_name").clear()
            driver.find_element(By.NAME, "group_name").send_keys(group.name)
            driver.find_element(By.NAME, "update").click()
            driver.find_element(By.LINK_TEXT, "groups").click()

    def count(self):
        driver = self.app.driver
        driver.find_element(By.LINK_TEXT, "groups").click()
        return len(driver.find_elements(By.XPATH, "//input[@type='checkbox']"))
