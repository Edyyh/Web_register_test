# coding = utf-8
from register.register_business import RegisterBusiness
from selenium import webdriver

class Case1(object):
    def __init__(self):
        driver = webdriver.Chrome()
        driver.get('http://www.5itest.cn/register')
        self.test_register = RegisterBusiness(driver)

    def test_register_email_error(self):
        email_error = self.test_register.register_email_error("asdasda@160", "asdfff", "123456", "d8gfd")
        if email_error == True:
            print('如注册成功，此case执行失败')

    def test_register_username_error(self):
        username_error = self.test_register.register_username_error("asdasdasd@163.com", "asdfff", "123456", "d8gfd")
        if username_error == True:
            print('如注册成功，此case执行失败')

    def test_register_password_error(self):
        password_error = self.test_register.register_password_error("asdasda@160.com", "asdfff", "123456", "d8gfd")
        if password_error == True:
            print('如注册成功，此case执行失败')

    def test_register_code_error(self):
        code_error = self.test_register.register_code_error("asdasda@160.com", "asdfff", "123456", "d8gfd")
        if code_error == True:
            print('如注册成功，此case执行失败')

    def test_register_pass(self):
        result = self.test_register.register_success("asdasda@160.com", "asdfff", "123456", "d8gfd")
        if result == True:
            print('注册成功')


if __name__ == '__main__':
    first = Case1()
    first.test_register_email_error()
    first.test_register_username_error()
    first.test_register_password_error()
    first.test_register_password_error()
    first.test_register_pass()