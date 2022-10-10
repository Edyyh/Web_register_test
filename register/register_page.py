# coding = utf-8
from register.find_element import FindElement


# 调用find_element和config来定位元素位置
class RegisterPage(object):
    def __init__(self, driver):
        self.fd = FindElement(driver)

    # 定位到邮箱输入框
    def get_email_element(self):
        return self.fd.get_element("user_email")

    # 定位到邮箱错误信息
    def get_email_error_msg_element(self):
        return self.fd.get_element("user_email_error_msg")

    # 定位到用户名输入框
    def get_username_element(self):
        return self.fd.get_element("user_name")

    # 定位到用户名错误信息
    def get_username_error_msg_element(self):
        return self.fd.get_element("user_username_error_msg")

    # 定位到密码输入框
    def get_password_element(self):
        return self.fd.get_element("password")

    # 定位到密码错误信息
    def get_password_error_msg_element(self):
        return self.fd.get_element("user_password_error_msg")

    # 定位到验证码图片
    def get_code_image_element(self):
        return self.fd.get_element("code_image")

    # 定位到验证码输入框
    def get_code_text_element(self):
        return self.fd.get_element("code_text")

    # 定位到验证码错误信息
    def get_code_error_msg_element(self):
        return self.fd.get_element("code_text_error_msg")

    # 定位到注册按钮
    def get_register_button_element(self):
        return self.fd.get_element("register_button")
