import functools

squ=functools.partial(pow,exp=2)

print(squ(3))