﻿﻿==================  广深小龙-测试/生产环境数据库的表名与字段对比 =====================


简介：有时候测试环境跑的很正常，一上线可能报错缺少一些字段，于是写了一个sql_diff直接运行，看结果。


1.conifg.py:修改你的测试/生产数据库连接信息。

2.run_cases.py:运行只需运行它，如：python run_cases.py


其余不需要关心，适当看下html报告或看控制台输出即可。

PS：小龙写得有点low，ddt只能通过excel进行先存储(咋整？)但基本可以使用，如果你有更好的点子欢迎提出。


关于我：在这里你将会了解到更多：https://www.cnblogs.com/gsxl/
