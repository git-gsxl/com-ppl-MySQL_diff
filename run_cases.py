# coding=utf-8
import unittest, os, sys
cur_path = os.getcwd()              # 声明路径
sys.path.append(cur_path)           # 添加至环境变量
import conifg, base, HTMLTestRunner

report_name = u'SQL字段对比.html'     # 报告名称
report_title = u'SQL字段对比测试'     # 报告title名称

c = conifg.config_sql()
exp = c[0]
res = c[1]
print('广深小龙提醒您，【测试环境】连接信息为：%s:%s，库名为：%s' % (exp['host'], exp['port'], exp['db']))
print('广深小龙提醒您，【生产环境】连接信息为：%s:%s，库名为：%s' % (res['host'], res['port'], res['db']))


def add_case(rule='test*.py'):
    '''第一步：加载所有的测试用例'''
    # 定义 discover 方法的参数，返回测试用例列表文件名
    discover = unittest.defaultTestLoader.discover(cur_path,
                                                   pattern=rule,
                                                   top_level_dir=None)
    return discover


def run_case(all_case):
    '''第二步：执行所有的用例, 把结果写入测试报告'''
    report_path = os.path.join(cur_path, report_name)   # 测试报告名称
    print('生成报告目录在:%s' % report_path)
    fp = open(report_path, 'wb')                        # 加载所有用例，写入测试报告，生成
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=report_title, retry=0)
    runner.run(all_case)                                # 执行
    fp.close()


if __name__ == '__main__':
    try: os.remove('excel.xls')
    except:pass

    base.Excel.wirte_data()     # 创建文件接收表信息
    all_case = add_case()       # 加载用例
    run_case(all_case)          # 执行用例
