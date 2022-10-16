# coding = utf-8
import ddddocr
from PIL import Image
from register.register_page import RegisterPage


class GetCode:
    def __init__(self, driver):
        self.driver = driver

    # 获取验证码图片
    def get_code_image(self, file_name):
        pg = RegisterPage(self.driver)
        self.driver.save_screenshot(file_name)
        code_element = pg.get_code_image_element()
        # self.driver.find_element(by=By.ID, value='getcode_num')
        left = code_element.location['x']  # 以左上角为原点，向右向下延伸的长方形
        top = code_element.location['y']
        right = code_element.size['width'] + left
        bottom = code_element.size['height'] + top
        image_screenshot = Image.open(file_name)
        image_cropped = image_screenshot.crop((left, top, right, bottom))
        image_cropped.save(file_name)

    # 从图片里提取验证码
    def get_code_from_image(self, file_name):
        self.get_code_image(file_name)
        ocr = ddddocr.DdddOcr()
        with open(file_name, 'rb') as f:
            img_bytes = f.read()
        text = ocr.classification(img_bytes)
        return text
