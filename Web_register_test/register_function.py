# coding = utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image
import time
import random
import ddddocr
import os
from find_element import FindElement


class RegisterFunction(object):

    def __init__(self, url, driver_index):
        self.driver = self.get_driver(url, driver_index)

    def get_driver(self, url, driver_index):
        if driver_index == 0:
            driver = webdriver.Chrome()
        elif driver_index == 1:
            driver = webdriver.Safari()
        else:
            driver = None

        driver.get(url)
        driver.maximize_window()
        return driver

    # 输入用户信息
    def input_user_info(self, key, data):
        self.get_user_element(key).send_keys(data)

    # 定位用户信息
    def get_user_element(self, key):
        find_element = FindElement(self.driver)
        user_element = find_element.get_element(key)
        return user_element

    def get_random_user(self):
        user_name = ''.join(random.sample('1234567890abcdefghijklmnopqrstuvwxyz', 8))
        return user_name

    # 获取验证码图片
    def get_code_image(self, file_name):
        self.driver.save_screenshot(file_name)
        code_element = self.get_user_element('code_image')
        left = code_element.location['x']  # 以左上角为原点，向右向下延伸的长方形
        top = code_element.location['y']
        right = code_element.size['width'] + left
        bottom = code_element.size['height'] + top
        image_screenshot = Image.open(file_name)
        image_cropped = image_screenshot.crop((left, top, right, bottom))
        image_cropped.save(file_name)

    def get_code_from_image(self, file_name):
        self.get_code_image(file_name)
        ocr = ddddocr.DdddOcr()
        with open(file_name, 'rb') as f:
            img_bytes = f.read()
        text = ocr.classification(img_bytes)
        return text

    def main(self):
        user_name_info = self.get_random_user()
        user_email = user_name_info + "@outlook.com"
        file_name = os.getcwd() + "/Image/test_pic.png"
        code_text = self.get_code_from_image(file_name)
        self.input_user_info("user_email", user_email)
        self.input_user_info("user_name", user_name_info)
        self.input_user_info("password", "111111")
        self.input_user_info("code_text", code_text)
        self.get_user_element("register_button").click()
        code_error = self.get_user_element("code_text_error_msg")

        if code_error == None:
            print("Successfully register")
        else:
            self.driver.save_screenshot(os.getcwd() + "/Image/test_code_error.png")


if __name__ == '__main__':
    for i in range(2):
        web = RegisterFunction("http://www.5itest.cn/register", i)
        web.main()
