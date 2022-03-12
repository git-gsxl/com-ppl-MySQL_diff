import pymysql, xlrd, os, xlwt
from xlrd import open_workbook
from xlutils.copy import copy
import conifg


class Excel:
    '''excelPath= excel 的目录路径，sheetName = 自定义table'''
    def __init__(self, excelPath, tableName='Sheet1'):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(tableName)
        self.keys = self.table.row_values(0)    # 获取第一行作为key值
        self.rowNum = self.table.nrows          # 获取总行数
        self.colNum = self.table.ncols          # 获取总列数

    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            r = []
            j = 1
            for i in range(self.rowNum-1):
                s = {}
                values = self.table.row_values(j)   # 从第二行取对应values值
                for x in range(self.colNum):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j += 1
            return r

    @staticmethod
    def wirte_data(report='excel.xls', test=False, exp_data=None, res_data=None, num=None):
        '''判断是否需要新建表格'''
        res_excel = os.path.isfile('excel.xls')
        if res_excel is False:
            workbook = xlwt.Workbook(encoding='utf-8')
            worksheet = workbook.add_sheet('Sheet1')
            worksheet.write(0, 0, label='exp_table')
            worksheet.write(0, 1, label='res_table')
            worksheet.write(0, 2, label='exp_field')
            worksheet.write(0, 3, label='res_field')
            worksheet.write(0, 5, label='ERROR')
            workbook.save('excel.xls')
        excel = copy(open_workbook(report, formatting_info=True))
        tables = excel.get_sheet('Sheet1')

        # 判断是否为test模式，该模式给与cases运行时使用，默认为：False
        if test:
            tables.write(num, 2, exp_data)
            tables.write(num, 3, res_data)
            tables.write(num, 5, True)

        else:
            exp_tlabe = SQL.table(SQL.send_sql())                  # 测试环境数据库
            res_tlabe = SQL.table(SQL.send_sql(exp=False))         # 生产环境数据库

            count = 0
            for i in exp_tlabe:
                count += 1
                tables.write(count, 0, i)
            count = 0
            for i in res_tlabe:
                count += 1
                tables.write(count, 1, i)

        excel.save(report)                                  # 保存并覆盖文件


class SQL:

    @staticmethod
    def send_sql(sql="show tables;", exp=True):
        # sql查询
        c = conifg.config_sql()
        if exp:
            host = c[0]['host']
            port = c[0]['port']
            user = c[0]['user']
            pwd = c[0]['pwd']
            db = c[0]['db']
        else:
            host = c[1]['host']
            port = c[1]['port']
            user = c[1]['user']
            pwd = c[1]['pwd']
            db = c[1]['db']

        try:
            db = pymysql.connect(
                host=host,
                port=port,
                user=user,
                passwd=pwd,
                db=db)

            cur = db.cursor()       # 使用 cursor() 方法创建一个游标对象cur
            cur.execute(sql)        # 使用 execute()  方法执行 SQL 查询
            data = cur.fetchall()   # 使用fetchall()方法获取查询结果 (接收全部的返回结果)
            db.commit()             # 提交执行
            db.close()              # 关闭连接
            return data

        except:
            return False

    @staticmethod
    def table(data):
        # 处理表名的
        lis = []
        if data:
            for i in data:
                for k in i:
                    lis.append(k)
            return lis
        else:
            return 'sql查询或连接错误，请检查您的配置以及sql语句！'

    @staticmethod
    def field(data):
        # 处理表各个字段的
        lis = []
        if data:
            for i in data:
                lis.append(i[0])
            return ','.join(lis)
        else:
            return 'sql查询或连接错误，请检查您的配置以及sql语句！'
