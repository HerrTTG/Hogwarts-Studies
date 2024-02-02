In = input()

exchangerate = 6.78

if In[0:3] == "USD":
    print("RMB{:.2f}".format(eval(In[3:]) * exchangerate))
elif In[0:3] == "RMB":
    print("USD{:.2f}".format(eval(In[3:]) / exchangerate))
else:
    print()
