# 不做研究只做应用，用到哪写到哪

from datetime import datetime
import xlrd


DATETIME_FMT = '%H:%M:%S'


class MyExcel():
    def __init__(self, xls, sheet_name='Sheet1'):
        self.xls, self.sheet_name = xls, sheet_name
        self.header, self.rows = self.read_excel_xls()
        self.to_dict()

    def read_excel_xls(self, xls='', sheet_name=''):
        """读取excel,返回字段名和数据(以行为单位) 
        [['name','local'],
         ['joe','china']]
        """
        xls = xls or self.xls
        sheet_name = sheet_name or self.sheet_name
        self.workbook = xlrd.open_workbook(xls)
        self.sheet = self.workbook.sheet_by_name(sheet_name)
        rows = []
        for row in range(self.sheet.nrows):
            line = []
            for col in range(self.sheet.ncols):
                line.append(self.dispaly_value(row, col))
            rows.append(line)
        header = rows.pop(0)
        return header, rows

    def dispaly_value(self, row, col):
        """return dispaly value which your edit"""
        # 兼容日期value为浮点数的情况
        value = self.sheet.cell(row, col)
        if 3 == value.ctype:
            date_tuple = xlrd.xldate_as_tuple(
                self.sheet.cell_value(row, col), self.workbook.datemode)
            return datetime(*date_tuple).strftime(DATETIME_FMT)
        return value

    def to_dict(self, header=None, rows=None):
        """行数据转json格式
        [{"name","joe"},{"local","china"}]
        """
        self.dict_table = []
        rows = rows or self.rows
        header = header or self.header
        for row in rows:
            d = {}
            for i in range(len(row)):
                key, value = header[i].split('/')[-1], row[i]
                d[key] = value
            self.dict_table.append(d)
