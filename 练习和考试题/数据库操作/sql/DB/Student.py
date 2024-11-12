from functools import cache

from DB.dbcontrol import Dbconnect


class StudentTable(Dbconnect):
    def __init__(self):
        super().__init__()

    @property
    @cache
    def all_student(self):
        return [Student(row) for row in self.query("select * from Student;")]

    def search_byfiled(self, filed, value, fetch_one=True):
        """select * from student where filed  =  value"""
        query = f"i.{filed}"

        for i in self.all_student:
            if eval(query) == value:
                print(i)
                if fetch_one:
                    break


class Student():

    def __init__(self, args):
        self.SId, self.Sname, self.Sage, self.Ssex = args

    def __str__(self):
        return f"<Student Sid={self.SId} Sname={self.Sname} Sage={self.Sage} Ssex={self.Ssex}>"
