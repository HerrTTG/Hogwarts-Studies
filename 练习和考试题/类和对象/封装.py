class Turtle:
    head=1
    eyes=2
    legs=4
    shell=True

    def crawl(self):
        print('人们总是抱怨我动作慢吞吞的，殊不知如不积蛙步，无以至千里的道理')

    def run(self):
        print('虽然我行动缓慢，但是遇到危险还是会拼命狂奔的')
    def bite(self):
        print('人善被人欺，我也是会咬人的')

    def eat(self):
        print('干饭人，干饭魂')

    def sleep(self):
        print('Zzzz...')

t1=Turtle()
print(t1.head)
print(t1.eyes)
t1.sleep()
print(dir(t1))