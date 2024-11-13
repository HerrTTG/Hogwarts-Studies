from functools import cached_property

from DB.dbcontrol import Dbconnect


class StudentTable(Dbconnect):
    def __init__(self):
        super().__init__()

    @cached_property
    def all_record(self):
        return [Student(row) for row in self.query("select * from Student;")]

    def search_byeq(self, filed, value, fetch_one=False):
        """select * from student where filed  =  value"""
        query = f"i.{filed}"

        for i in self.all_record:
            if eval(query) == value:
                print(i)
                if fetch_one:
                    break

    def search_bylike(self, filed, value, fetch_one=False):
        """select * from student where filed like value"""
        query = f"i.{filed}"

        for i in self.all_record:
            if value in eval(query):
                print(i)
                if fetch_one:
                    break

    def search_byin(self, filed, *value, fetch_one=False):
        """select * from student where filed in (value....)"""
        query = f"i.{filed}"

        for i in self.all_record:
            if eval(query) in value:
                print(i)
                if fetch_one:
                    break



class Student():

    def __init__(self, args):
        self.SId, self.Sname, self.Sage, self.Ssex = args

    def __str__(self):
        return f"<Student Sid={self.SId} Sname={self.Sname} Sage={self.Sage} Ssex={self.Ssex}>"
