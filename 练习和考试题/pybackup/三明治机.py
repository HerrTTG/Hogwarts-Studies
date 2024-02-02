import  pyinputplus,sys,time

def menuask():
    ls=[]
    try:
        ls.append(pyinputplus.inputMenu(['wheat','white','sourdough'],\
                                    'Would you like some bread? We offer the following types:\n',\
                                     timeout=30,limit=3,blank=True))
        time.sleep(1)
        ls.append(pyinputplus.inputMenu(['chicken', 'turkey', 'ham','tofu'], \
                                        'About protein ,We offer the following types:\n', \
                                        timeout=30, limit=3,blank=True))
        time.sleep(1)
        if pyinputplus.inputYesNo('Would you like some cheese?',timeout=30, limit=3) in ['Yes','yes','Y','y','YES']:
            ls.append(pyinputplus.inputMenu(['cheddar','Swiss','mozzarella'],'What kind of chess would you like?\n',\
                                            timeout=30, limit=3,blank=True))
        time.sleep(1)
        if pyinputplus.inputYesNo('Did need mayo、mustard、lettuce or tomato?',timeout=30, limit=3) in ['Yes','yes','Y','y','YES']:
            s=''
            for i in range(4):
                s = pyinputplus.inputMenu(['mayo', 'mustard', 'lettuce', 'tomato'], 'What kind of would you like?\n', \
                                          timeout=30, limit=3, blank=True)
                if s is None :
                    break
                else:
                    ls.append(s)
        time.sleep(1)
        n=pyinputplus.inputInt('How much subway did you want?',timeout=30, limit=3)
        return n,ls

    except pyinputplus.TimeoutException:
        print('Long time no response, service ended. Looking forward to your next visit!')
        sys.exit(1)
    except pyinputplus.RetryLimitException:
        print('Too many input errors, service ended. Looking forward to your next visit!')
        sys.exit(1)

def col_price(n,menu):
    map={'wheat':2,'white':1,'sourdough':3,'chicken':5,'turkey':3,'ham':4,'tofu':2,'cheddar':3,'Swiss':3,'mozzarella':3\
         ,'mayo':2,'mustard':1,'lettuce':0,'tomato':1}
    sum=0.0
    for i in menu:
        sum=sum+map[i]
    return n*sum

def main():
    intro='''Wellcome subway!'''
    while True:
        print(intro)
        time.sleep(1)
        n,menu=menuask()
        print('Your subway have : {} ,and this is the menu of it {}'.format(n,menu))
        time.sleep(1)
        try :
            if pyinputplus.inputYesNo('Comfirme yes or no ?',timeout=60, limit=3) in ['Yes', 'yes', 'Y', 'y', 'YES']:
                    print('Thank you for choosing the subway. Your total consumption is: '.format(col_price(n,menu)))
                    break
            else:
                    print('Thank you for choosing the subway. Looking forward to your next visit!')
                    time.sleep(3)
                    continue
        except pyinputplus.TimeoutException:
                print('Long time no response, service ended. Looking forward to your next visit!')
                sys.exit(1)
        except pyinputplus.RetryLimitException:
                print('Too many input errors, service ended. Looking forward to your next visit!')
                sys.exit(1)

main()