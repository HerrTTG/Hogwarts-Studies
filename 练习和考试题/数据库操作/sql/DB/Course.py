from functools import cached_property

from DB.dbcontrol import Dbconnect


class CourseTable(Dbconnect):
    def __init__(self):
        super().__init__()

    @cached_property
    def all_record(self):
        return [Course(row) for row in self.query("select * from Course;")]

    def search_byeq(self, filed, value, fetch_one=False):
        query = f"i.{filed}"
        for i in self.all_record:
            if eval(query) == value:
                print(i)
                if fetch_one:
                    break


class Course():

    def __init__(self, args):
        self.CId, self.Cname, self.TId = args

    def __str__(self):
        return f"<Coure CId={self.CId} Cname={self.Cname} TId={self.TId}>"
