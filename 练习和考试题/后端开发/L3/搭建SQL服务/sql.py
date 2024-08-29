import sqlparse

from dto import Db_serve


class sql_parse_demo:
    def __init__(self, sql):
        # 获取sql字符串，使用sqlparse库进行解析
        self.sql = sql
        self.parsed = sqlparse.parse(sql)
        self.dto = Db_serve()

    # 解析规则
    def rule(self):
        # 初始化解析结果
        parsed = self.parsed[0]
        token_list = parsed.tokens
        # 获取SQL类型，对SQL进行初步解析
        type_sql = parsed.get_type()
        if type_sql == 'SELECT':
            return self.dto.search_serve(sql_str=self.sql, value_list=None)
        elif type_sql == 'UPDATE':
            pass
        elif type_sql == 'DELETE':
            pass
        elif type_sql == 'INSERT':
            pass
        else:
            pass

        # #通过比较SQL解析结果token_list中不同元件的属性来捕获SQL字符串的各个组成部分
        # for i in token_list:
        #    if isinstance(token_list[i], sqlparse.sql.Where):
        #       pass
        # #如果SQL检验通过，则将SQL语句交由DAO层代码进行执行，如果不通过则终止
