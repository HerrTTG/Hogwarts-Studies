class Display:
    def display(self,msg):
        print(msg)

class Logmix:
    def log(self,msg,filename='123.log'):
        print(msg+filename)
    def display(self,msg):
        super().display(msg)
        self.log(msg)

class Subclass(Logmix,Display):
    def log(self,msg):
        super().log(msg,filename='test.log')

subclass=Subclass()
subclass.display('Mix test')

