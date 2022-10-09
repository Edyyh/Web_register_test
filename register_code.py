# coding=utf-8
import ddddocr
from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image
import time
import random

driver = webdriver.Chrome()


def driver_initial():
    driver.get("http://www.5itest.cn/register")
    driver.maximize_window()
    time.sleep(2)


def get_element(id):
    user_id = driver.find_element(by=By.ID, value=id)
    return user_id


def get_random_user():
    user_name = ''.join(random.sample('1234567890abcdefghijklmnopqrstuvwxyz', 8))
    return user_name


# 获取验证码图片
def get_code_image(file_name):
    driver.save_screenshot(file_name)
    code_element = driver.find_element(by=By.ID, value="getcode_num")
    left = code_element.location['x']  # 以左上角为原点，向右向下延伸的长方形
    top = code_element.location['y']
    right = code_element.size['width'] + left
    bottom = code_element.size['height'] + top
    image_screenshot = Image.open(file_name)
    image_cropped = image_screenshot.crop((left, top, right, bottom))
    image_cropped.save(file_name)


def get_code_from_image(file_name):
    ocr = ddddocr.DdddOcr()
    with open(file_name, 'rb') as f:
        img_bytes = f.read()
    text = ocr.classification(img_bytes)
    return text


def main():
    user_name_info = get_random_user()
    user_email = user_name_info + "@163.com"
    file_name = "/Users/air/PycharmProjects/seleniumPython/Image/test_pic.png"

    driver_initial()
    get_element("register_email").send_keys(user_email)
    get_element("register_nickname").send_keys(user_name_info)
    get_element("register_password").send_keys("111111")
    get_code_image(file_name)
    text = get_code_from_image(file_name)
    get_element("captcha_code").send_keys(text)
    time.sleep(5)
    get_element("register-btn").click()


if __name__ == '__main__':
    main()

