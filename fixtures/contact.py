import re

from selenium.webdriver.common.by import By

from models.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def change_field_value(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element(By.NAME, field_name).click()
            driver.find_element(By.NAME, field_name).clear()
            driver.find_element(By.NAME, field_name).send_keys(text)

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            driver = self.app.driver
            self.open_home_page()
            self.contact_cache = []
            for row in driver.find_elements(By.NAME, "entry"):
                cells = row.find_elements(By.TAG_NAME, "td")
                firstname = cells[1].text
                lastname = cells[2].text
                id = cells[0].find_element(By.TAG_NAME, "input").get_attribute("value")
                all_phones = cells[5].text.splitlines()
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id,
                                                  homephone=all_phones[0], mobilephone=all_phones[1],
                                                  workphone=all_phones[2], secondaryphone=all_phones[3]))
            return list(self.contact_cache)

    def get_contact_from_view_page(self, index):
        driver = self.app.driver
        self.open_contact_view_by_index(index)
        text = driver.find_element(By.ID, "content").text
        homephone = re.search("H: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone, workphone=workphone, secondaryphone=secondaryphone)

    def open_home_page(self):
        driver = self.app.driver
        if driver.current_url.startswith("addressbook/"):
            if len(driver.find_elements(By.NAME, "entry")) > 0:
                return
        driver.find_element(By.XPATH, '//a[normalize-space()="home"]').click()

    def open_contact_to_edit_by_index(self, index):
        driver = self.app.driver
        self.open_home_page()
        row = driver.find_elements(By.NAME, "entry")[index]
        cell = row.find_elements(By.TAG_NAME, "td")[7]
        cell.find_element(By.TAG_NAME, "a").click()

    def open_contact_view_by_index(self, index):
        driver = self.app.driver
        self.open_home_page()
        row = driver.find_elements(By.NAME, "entry")[index]
        cell = row.find_elements(By.TAG_NAME, "td")[6]
        cell.find_element(By.TAG_NAME, "a").click()

    def get_contact_info_from_edit_page(self, index):
        driver = self.app.driver
        self.open_contact_to_edit_by_index(index)
        firstname = driver.find_element(By.NAME, "firstname").get_attribute("value")
        lastname = driver.find_element(By.NAME, "lastname").get_attribute("value")
        id = driver.find_element(By.NAME, "id").get_attribute("value")
        homephone = driver.find_element(By.NAME, "home").get_attribute("value")
        mobilephone = driver.find_element(By.NAME, "mobile").get_attribute("value")
        workphone = driver.find_element(By.NAME, "work").get_attribute("value")
        secondaryphone = driver.find_element(By.NAME, "phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, homephone=homephone,
                       mobilephone=mobilephone, workphone=workphone, secondaryphone=secondaryphone)
