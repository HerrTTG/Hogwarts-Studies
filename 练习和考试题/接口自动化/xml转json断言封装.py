import jsonpath
import requests
import xmltodict


class Testcase:
    @classmethod
    def xml_to_dict(self, response):
        """
        封装一个方法，判断响应体的格式。利用其他第三方库，将响应转为json格式，方便后续进行断言。
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

    def testcase1(self):
        r = requests.request("GET", 'https://www.nasa.gov/rss/dyn/lg_image_of_the_day.rss', verify=False)
        res = Testcase.xml_to_dict(r)
        # print(res)
        print(jsonpath.jsonpath(res, '$..link'))
