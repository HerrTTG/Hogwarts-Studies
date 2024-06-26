from frame.apis.BaseAPI import BaseAPI
from frame.domin.Address_book.member_domin import Member_domin
from frame.untils.loginAuth import LoginAuth


class Memebr(Member_domin, LoginAuth, BaseAPI):
    """
    成员管理接口的方法实现
    """

    def create(self, memberdata) -> object:
        """
        memberdata:字典格式，来自于testdata_memberinfo.yaml文件中提取
        """

        url = self.baseurl + 'user/create'
        r = self.send('address_book', 'POST', url, json=memberdata, verify=False)
        return r

    def delete(self, memberdata) -> object:
        """
        memberdata:{'userid': self.memberdata['userid']}
        """
        url = self.baseurl + 'user/delete'
        r = self.send('address_book', 'GET', url, params=memberdata, verify=False)
        return r

    def list(self, requestbody) -> object:
        """
        requestbody:{"limit": 10000}
        """
        url = self.baseurl + 'user/list_id'
        r = self.send('address_book', 'POST', url, json=requestbody, verify=False)
        return r
