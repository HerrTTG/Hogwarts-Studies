from frame.apis.BaseAPI import BaseAPI
from frame.domin.Address_book.department_domin import Department_domin


class Department(BaseAPI, Department_domin):

    def create(self, departdata):
        url = self.baseurl + '/cgi-bin/department/create'
        r = self.send('department', 'POST', url, json=departdata, verify=False)
        return r


    def update(self):
        pass

    def delete(self, params):
        url = self.baseurl + '/cgi-bin/department/delete'
        r = self.send('department', 'GET', url, params=params, verify=False)
        return r

    def simplelist(self, params):
        url = self.baseurl + '/cgi-bin/department/simplelist'
        r = self.send('department', 'GET', url, params=params, verify=False)
        return r
