# coding = utf-8
from register.register_handle import RegisterHandle


class RegisterBusiness(object):
    def __init__(self, driver):
        self.register_handle = RegisterHandle(driver)

    # 模拟用户操作
    def register_base(self, email, name, password, image_path):
        self.register_handle.input_user_email(email)
        self.register_handle.input_user_name(name)
        self.register_handle.input_user_password(password)
        self.register_handle.input_user_code(image_path)
        self.register_handle.click_register_button()

    def register_success(self, email, name, password, image_path):
        self.register_base(email, name, password, image_path)
        if self.register_handle.get_register_button_text() == None:
            return True
        else:
            return False

    # 输入邮箱错误
    def register_email_error(self, email, name, password, image_path):
        self.register_base(email, name, password, image_path)
        if self.register_handle.get_register_error_msg('user_email_error_msg', '请输入有效的电子邮件地址') == None:
            print('邮箱检验不成功')
            return True
        else:
            return False

    # 输入用户名错误
    def register_username_error(self, email, name, password, image_path):
        self.register_base(email, name, password, image_path)
        if self.register_handle.get_register_error_msg('user_username_error_msg', '字符长度必须大于等于4，一个中文字算2个字符') == None:
            print('用户名检验不成功')
            return True
        else:
            return False

    # 输入密码错误
    def register_password_error(self, email, name, password, image_path):
        self.register_base(email, name, password, image_path)
        if self.register_handle.get_register_error_msg('user_password_error_msg', '最少需要输入 5 个字符') == None:
            print('密码检验不成功')
            return True
        else:
            return False

    # 输入验证码错误
    def register_code_error(self, email, name, password, image_path):
        self.register_base(email, name, password, image_path)
        if self.register_handle.get_register_error_msg('code_text_error_msg', '必须是英文字母、数字及下划线组成') == None:
            print('验证码检验不成功')
            return True
        else:
            return False
