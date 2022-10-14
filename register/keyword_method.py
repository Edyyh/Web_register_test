# coding = utf-8
from selenium import webdriver
from register.find_element import FindElement
import time


class ActionMethod:

    def open_browser(self, browser):
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'safari':
            self.driver = webdriver.Safari()

    def get_url(self, url):
        self.driver.get(url)

    def get_element(self, key):
        fd = FindElement(self.driver)
        element = fd.get_element(key)
        return element

    def element_input_value(self, key, value):
        element = self.get_element(key)
        element.send_keys(value)

    def click_element(self, key):
        self.get_element(key)

    def sleep_time(self):
        time.sleep(3)

    def close_browser(self):
        self.driver.close()
