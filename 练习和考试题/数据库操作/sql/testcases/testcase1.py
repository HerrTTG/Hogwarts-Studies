from DB.Student import StudentTable
from DB.dbcontrol import Dbconnect


def test():
    db_exetor = Dbconnect()
    assert db_exetor.create_tables()
    assert db_exetor.insert_data()


def test2():
    db_exetor = StudentTable()
    for i in db_exetor.all_student:
        print(i)


def test3():
    db_exetor = StudentTable()
    db_exetor.search_byfiled("SId", "02")


def test4():
    db_exetor = StudentTable()
    db_exetor.search_byfiled("Sname", "李小刀")


def test5():
    db_exetor = StudentTable()
    db_exetor.search_byfiled("Sage", "1998-01-01 00:00:00", fetch_one=False)


def test6():
    db_exetor = StudentTable()
    db_exetor.search_byfiled("Ssex", "女", fetch_one=False)
