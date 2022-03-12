import unittest, ddt
import base
b = base
test_data = b.Excel('excel.xls').dict_data()
n = 0

@ddt.ddt
class Test_Diff(unittest.TestCase):

    @ddt.data(*test_data)
    def test_diff_table(self, data):
        exp = data['exp_table']
        res = data['res_table']
        self.assertEqual(exp, res, "测试环境表：%s != 生产环境表：%s" % (exp, res))

    @ddt.data(*test_data)
    def test_diff_field(self, data):
        global n
        n += 1
        exp = b.SQL.field(b.SQL.send_sql("describe %s;" % data['exp_table']))
        res = b.SQL.field(b.SQL.send_sql("describe %s;" % data['res_table'], exp=False))
        if exp != res:
            b.Excel.wirte_data(test=True, num=n, exp_data=exp, res_data=res)
        self.assertEqual(exp, res, "测试环境字段：%s != 生产环境字段：%s  测试环境表名为：%s" % (exp, res, data['exp_table']))
