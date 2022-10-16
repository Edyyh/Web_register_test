# coding = utf-8
from util.excel_util import ExcelUtil
from register.keyword_method import ActionMethod


class KeywordCase:
    def run_main(self):
        self.action_method = ActionMethod()
        excel_path = ExcelUtil('/Users/air/PycharmProjects/Web_register_test/config/keyword.xls')
        case_lines = excel_path.get_lines()
        if case_lines:
            for i in range(1, case_lines):
                is_run = excel_path.get_cell_value(i, 3)
                if is_run == 'yes':
                    method = excel_path.get_cell_value(i, 4)
                    input_value = excel_path.get_cell_value(i, 5)
                    element = excel_path.get_cell_value(i, 6)
                    expect_result = excel_path.get_cell_value(i, 7)
                    actual_result = excel_path.get_cell_value(i, 8)
                    # if input_value:
                    self.run_method(method, input_value, element)
                    if actual_result != '':
                        expect_value = self.get_expect_result_value(actual_result)
                        if expect_value[0] == 'text':
                            result = self.run_method(expect_result)
                            if expect_value[1] in result:
                                excel_path.write_value(i, 'pass')
                            else:
                                excel_path.write_value(i, 'fail')
                        elif expect_value[0] == 'element':
                            result = self.run_method(expect_result, expect_value[1])
                            if result:
                                excel_path.write_value(i, 'pass')
                            else:
                                excel_path.write_value(i, 'fail')
                        else:
                            print('没有else')
                    else:
                        print('预期结果为空')

    def get_expect_result_value(self, data):
        return data.split('=')

    def run_method(self, method, input_value='', element=''):
        method_value = getattr(self.action_method, method)
        if input_value == '' and element != '':
            result = method_value(element)
        elif input_value == '' and element == '':
            result = method_value()
        elif input_value != '' and element == '':
            result = method_value(input_value)
        else:
            result = method_value(input_value, element)
        return result


if __name__ == '__main__':
    test = KeywordCase()
    test.run_main()
