# coding = utf-8
from register.register_business import RegisterBusiness
from selenium import webdriver
# from log.user_log import UserLog
import unittest
import os
import time
import HTMLTestRunner


class Case1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.image_path = '/Users/air/PycharmProjects/Web_register_test/Image/test_pic.png'

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://www.5itest.cn/register')
        self.test_register = RegisterBusiness(self.driver)

    def tearDown(self):
        time.sleep(2)
        errors = self._outcome.errors
        for method_name, error in errors:
            case_name = self._testMethodName
            report_screenshot_path = os.path.join(
                os.path.abspath(os.path.join(os.getcwd(), "..")) + '/report/' + case_name + '.png')
            self.driver.save_screenshot(report_screenshot_path)

        self.driver.close()
        print('teardown')

    def test_register_email_error(self):
        email_error = self.test_register.register_email_error("11111111@160", "11111111", "123456", self.image_path)
        self.assertFalse(email_error, 'case ran')
        # if email_error == True:
        #     print('如注册成功，此case执行失败')

    def test_register_username_error(self):
        username_error = self.test_register.register_username_error("2222222@163.com", "222222222", "123456",
                                                                    self.image_path)
        self.assertFalse(username_error)

    def test_register_password_error(self):
        password_error = self.test_register.register_password_error("333333333@160.com", "33333333", "123456",
                                                                    self.image_path)
        self.assertFalse(password_error)

    def test_register_code_error(self):
        code_error = self.test_register.register_code_error("44444444@160.com", "4444444444", "123456", self.image_path)
        self.assertFalse(code_error)

    def test_register_pass(self):
        result = self.test_register.register_success("55555555555@160.com", "55555555", "123456", self.image_path)
        self.assertTrue(result)


if __name__ == '__main__':
    # first = Case1()
    # first.test_register_email_error()
    # first.test_register_username_error()
    # first.test_register_password_error()
    # first.test_register_code_error()
    # first.test_register_pass()
    file_path = os.path.join(os.path.abspath(os.path.join(os.getcwd(), "..")) + '/report/' + 'first_report.html')
    f = open(file_path, 'wb')
    suite = unittest.TestSuite()
    suite.addTest(Case1('test_register_email_error'))
    # suite.addTest(Case1('test_register_username_error'))
    # suite.addTest(Case1('test_register_password_error'))
    # suite.addTest(Case1('test_register_code_error'))
    # suite.addTest(Case1('test_register_pass'))
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="Test Cases Report", description=u"第一次测试报告",
                                           verbosity=2)
    runner.run(suite)
    # unittest.main()
