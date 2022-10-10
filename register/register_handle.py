# coding = utf-8
from register.register_page import RegisterPage


# 通过register_page定位到元素位置，再进行内容输入
class RegisterHandle(object):
    def __init__(self, driver):
        self.register_page = RegisterPage(driver)

    # 输入邮箱
    def input_user_email(self, email):
        self.register_page.get_email_element().send_keys(email)

    # 输入用户名
    def input_user_name(self, username):
        self.register_page.get_username_element().send_keys(username)

    # 输入密码
    def input_user_password(self, password):
        self.register_page.get_password_element().send_keys(password)

    # 输入验证码
    def input_user_code(self, code):
        self.register_page.get_code_element().send_keys(code)

    # 点击注册按钮
    def click_register_button(self):
        self.register_page.get_register_button_element().click()

    def get_register_error_msg(self, msg, msg_text):
        try:
            if msg == 'user_email_error_msg':
                text = self.register_page.get_email_error_msg_element().text
            elif msg == 'user_username_error_msg':
                text = self.register_page.get_username_error_msg_element().text
            elif msg == 'user_password_error_msg':
                text = self.register_page.get_password_error_msg_element().text
            else:
                text = self.register_page.get_code_error_msg_element().text
        except:
            text = None

        print(text)
        return text

    # 获取注册按钮文字
    def get_register_button_text(self):
        return self.register_page.get_register_button_element().text
