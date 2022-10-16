# coding = utf-8
import xlrd
from xlutils.copy import copy


class ExcelUtil:
    def __init__(self, excel_path=None, index=None):
        if excel_path == None:
            self.excel_path = '/Users/air/PycharmProjects/Web_register_test/config/register_data.xls'
        else:
            self.excel_path = excel_path
        if index == None:
            index = 0

        self.data = xlrd.open_workbook(excel_path)
        self.table = self.data.sheets()[index]

    def get_data(self):
        result = []
        rows = self.get_lines()
        if rows != None:
            for i in range(self.get_lines()):
                row = self.table.row_values(i)
                result.append(row)
            return result
        return None

    def get_lines(self):
        rows = self.table.nrows
        if rows >= 1:
            return rows
        return None

    def get_cell_value(self, row, col):
        if self.get_lines() > row:
            cell_value = self.table.cell(row, col).value
            return cell_value
        return None

    def write_value(self, row, value):
        read_value = xlrd.open_workbook(self.excel_path)
        write_date = copy(read_value)
        write_date.get_sheet(0).write(row, 9, value)
        write_date.save(self.excel_path)


if __name__ == '__main__':
    excel = ExcelUtil('/Users/air/PycharmProjects/Web_register_test/config/keyword.xls')
