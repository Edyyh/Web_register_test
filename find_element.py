# coding = utf-8
from selenium.webdriver.common.by import By

from util.read_ini import ReadIni


class FindElement(object):

    def __init__(self, driver):
        self.driver = driver
#dsfsdfsdfdsf
    def get_element(self, key):
        read_ini = ReadIni()
        data = read_ini.get_value(key)
        by = data.split(' > ')[0]
        value = data.split(' > ')[1]

        try:
            if by == 'id':
                return self.driver.find_element(by=By.ID, value=value)
            elif by == 'name':
                return self.driver.find_element(by=By.NAME, value=value)
            elif by == 'className':
                return self.driver.find_element(by=By.CLASS_NAME, value=value)
            else:
                return self.driver.find_element(by=By.XPATH, value=value)
        except:
            return None
