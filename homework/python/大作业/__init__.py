"""
完成学生管理系统的多任务Web服务器
以面向对象方式实现，使用字典表示学生信息，不需要封装学生类
实现增删改查接口，返回 json 格式数据

请求方式：
主页： http://127.0.0.1:8080/
添加： http://127.0.0.1:8080/add?sid=09&name=lucy&age=23&gender=male
修改： http://127.0.0.1:8080/change?sid=09&name=kevin&age=23&gender=male
查询： http://127.0.0.1:8080/query?sid=09
查询全部： http://127.0.0.1:8080/query?sid=all
删除： http://127.0.0.1:8080/del?sid=09

修改支持只修改name或者age或者gender，但必须有其中之一传入
添加支持name或者age或者gender为空，但必须其中一个有值

数据存放在数据库中
数据库创建名:'hogwarts'
数据库port:3306
数据库表配置：
tablename=students sid(主键，int类型) name(varchar) age(varchar) gender(varchar)
"""

__all__ = ['Webservice', 'stdatabase']
