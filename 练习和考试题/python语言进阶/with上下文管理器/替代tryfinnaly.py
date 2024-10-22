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

        # json.loads({'a'}) 会发生异常
        # 所以在上下文管理对象结束时，调用__exit__(self, exc_type, exc_val, exc_tb)

        # 判断用户构造时传入了可原谅的错误类型，并比对exc_type是否何其一致。
        if self.exception_type and exc_type is self.exception_type:
            print(exc_type, exc_val, exc_tb)
            print(1)
            return self

        #如果不是指定错误类型，则返回False交由外部异常捕获进行处理
        elif self.exception_type is None and issubclass(exc_type, Exception):
            return False


# try:
#     json.loads({'a'})
# except TypeError as e:
#     print(type(e),e)
# finally:
#     print(1)


with A(TypeError) as a:
    json.loads({'a'})
