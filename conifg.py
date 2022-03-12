def config_sql():

    exp_dic = {                     # 【测试】环境数据库配置
        'host': 'localhost',
        'port': 3306,
        'user': 'root',
        'pwd': '123456',
        'db': 'test_web'}

    res_dic = {                     # 【生产】环境数据库配置
        'host': 'localhost',
        'port': 3306,
        'user': 'root',
        'pwd': '123456',
        'db': 'web'}

    return exp_dic, res_dic
