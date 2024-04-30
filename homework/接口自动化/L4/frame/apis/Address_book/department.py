from frame.apis.BaseAPI import BaseAPI
from frame.domin.Address_book.department_domin import Department_domin


class Department(BaseAPI, Department_domin):
    """
    部门管理接口的方法实现
    """

    def create(self, departdata):
        """
        departdata：{
            "name": "广州研发中心",
            "name_en": "RDGZ",
            "parentid": 1,
            "order": 1,
            "id": 2}
        创建部门的具体信息
        """
        url = self.baseurl + '/cgi-bin/department/create'
        r = self.send('department', 'POST', url, json=departdata, verify=False)
        return r


    def update(self):
        pass

    def delete(self, params):
        """
        params={'id': 2}
        要删除的目标部门id
        """
        url = self.baseurl + '/cgi-bin/department/delete'
        r = self.send('department', 'GET', url, params=params, verify=False)
        return r

    def simplelist(self, params):
        """
        params={'id': 2}
        要查询的目标部门id
        """
        url = self.baseurl + '/cgi-bin/department/simplelist'
        r = self.send('department', 'GET', url, params=params, verify=False)
        return r
