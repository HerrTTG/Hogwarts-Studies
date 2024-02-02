import  pyinputplus
import random,time

numerofquestions=10
correcttimes=0

for question in range(numerofquestions):
    num1=random.randint(0,9)
    num2=random.randint(0,9)
    prompt='#{}:{} x {} = '.format(question+1,num1,num2)
    try:
        pyinputplus.inputStr(prompt,allowRegexes=['^{}$'.format(num1*num2)],blockRegexes=[('.*','Incorrect!')],timeout=8,limit=3)
    except pyinputplus.TimeoutException:
        print('Out time out')
        continue
    except pyinputplus.RetryLimitException:
        print('Out of tries')
        continue
    else:
        print('correct')
        correcttimes+=1
        time.sleep(1)
print(correcttimes)

