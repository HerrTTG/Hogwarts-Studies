import threading,time

print('start')
def testsleep():
    time.sleep(5)
    return print('wake up')

throbj=threading.Thread(target=testsleep)
throbj.start()
print('end')