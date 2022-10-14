# coding = utf-8
from util.excel_util import ExcelUtil
from register.keyword_method import ActionMethod


class KeywordCase():
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
                    if input_value:
                        self.run_method(method, input_value, element)

    def run_method(self, method, input_value, element):
        method_value = getattr(self.action_method, method)
        if input_value:
            method_value(input_value, element)
        else:
            method_value(element)


if __name__ == '__main__':
    test = KeywordCase()
    test.run_main()
