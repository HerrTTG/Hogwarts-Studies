from DB.Course import CourseTable
from DB.Student import StudentTable
from DB.dbcontrol import Dbconnect


def test():
    db_exetor = Dbconnect()
    assert db_exetor.create_tables()
    assert db_exetor.insert_data()


def test2():
    db_exetor = StudentTable()
    for i in db_exetor.all_record:
        print(i)


def test3():
    db_exetor = StudentTable()
    db_exetor.search_byeq("SId", "02")


def test4():
    db_exetor = StudentTable()
    db_exetor.search_byeq("Sname", "李小刀")


def test5():
    db_exetor = StudentTable()
    db_exetor.search_byeq("Sage", "1998-01-01 00:00:00", fetch_one=True)


def test6():
    db_exetor = StudentTable()
    db_exetor.search_byeq("Ssex", "女", fetch_one=False)


def test7():
    db_exetor = CourseTable()
    db_exetor.search_byeq("Cname", "母猪产后护理")


def test8():
    db_exetor = StudentTable()
    db_exetor.search_bylike("Sname", "李")


def test9():
    db_exetor = StudentTable()
    db_exetor.search_byin("SId", "01", "02", "03")
