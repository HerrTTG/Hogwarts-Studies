import os
import sys

workpath = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(workpath)
from CK290520.func.books import Books

if __name__ == '__main__':
    op = Books(workpath)
    op.bookManager()
