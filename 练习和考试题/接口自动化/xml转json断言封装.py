import jsonpath
import requests
import xmltodict


class Restransf:
    """
    二次封装一个类，用于转换消息体中不同的格式。
    """
    @classmethod
    def res_to_dict(self, response):
        """
        定义一个类方法，判断响应体的格式。利用其他第三方库，将响应转为json格式，方便后续进行断言。
        """
        res_text = response.text
        # 判断为xml 调用xmltodict，转为json格式
        if res_text.startswith("<?xml"):
            final_res = xmltodict.parse(res_text)
        # 判断为html，后续可以找方法转为json
        elif res_text.startswith("<?DOCTYPE html"):
            final_res = 'HTML 格式'
        else:
            final_res = response.json()
        return final_res


def testcase1():
    r = requests.request("GET", 'https://www.nasa.gov/rss/dyn/lg_image_of_the_day.rss', verify=False)
    res = Restransf.res_to_dict(r)
    # print(res)
    print(jsonpath.jsonpath(res, '$..link'))
