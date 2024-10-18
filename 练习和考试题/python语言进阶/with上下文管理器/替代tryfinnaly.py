import json


class A():
    def __init__(self, exception_type=None):
        # 构造时传入异常类型
        self.exception_type = exception_type

    def __enter__(self):
        """
        上下文管理器进入时的处理
        """
        return self  # 返回self，给as 后的变量进行赋值

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        无论with中间的代码运行是否出现异常，都对最终执行exit方法。
        没有发生异常，或者中间代码出现return/break/continue等跳出语句
        则以exit(None,None,None)调用，
        如果发生异常，且exit返回False,则由外部程序继续捕获异常。
        """
        if self.exception_type and exc_type is self.exception_type:
            print(exc_type, exc_val, exc_tb)
            print(1)
            return self

        elif self.exception_type is None and issubclass(exc_type, Exception):
            raise exc_type


# try:
#     json.loads({'a'})
# except Exception as e:
#     print(e)
# finally:
#     print(1)


with A(TypeError) as a:
    json.loads({'a'})
