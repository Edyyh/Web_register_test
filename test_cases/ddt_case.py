# coding = utf-8
from register.register_business import RegisterBusiness
from util.excel_util import ExcelUtil
from selenium import webdriver
# from log.user_log import UserLog
import unittest
import os
import time
import ddt
import HTMLTestRunner

excel = ExcelUtil()
data = excel.get_data()


# email, username, password, code, error-msg
@ddt.ddt
class DdtCase(unittest.TestCase):

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

    # @ddt.data(
    #     ['11111111@outlook.com', 'edyyh', 'asdasdasd', 'code', 'user_email_error_msg', '请输入有效的电子邮件地址']
    #     # ['22222222', 'edyyh', 'asdasdasd', 'code', 'user_email_error_msg', '请输入有效的电子邮件地址'],
    #     # ['33333333@outlook.com', 'edyyh', 'asdasdasd', 'code', 'user_email_error_msg', '请输入有效的电子邮件地址']
    # )
    # @ddt.unpack

    @ddt.data(*data)
    def test_register_case(self, data):
        email, username, password, code_image, assertCode, assertText = data
        email_error = self.test_register.register_function(email, username, password, self.image_path, assertCode,
                                                           assertText)
        self.assertFalse(email_error, 'case failed')


if __name__ == '__main__':
    # file_path = os.path.join(os.path.abspath(os.path.join(os.getcwd(), "..")) + '/report/' + 'first_report.html')
    # f = open(file_path, 'wb')
    # suite = unittest.TestLoader().loadTestsFromTestCase(DdtCase)
    # runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="Test Cases Report", description=u"第一次测试报告",
    #                                        verbosity=2)
    # runner.run(suite)
    # unittest.main()
    pass
