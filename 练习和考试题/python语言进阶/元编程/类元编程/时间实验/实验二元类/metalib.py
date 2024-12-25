# tag::METALIB_TOP[]
print('% metalib module start')

import collections


class NosyDict(collections.UserDict):
    def __setitem__(self, key, value):
        args = (self, key, value)
        print(f'% NosyDict.__setitem__{args!r}')
        super().__setitem__(key, value)

    def __repr__(self):
        return '<NosyDict instance>'


# end::METALIB_TOP[]

# tag::METALIB_BOTTOM[]
class MetaKlass(type):
    print('% MetaKlass body')

    @classmethod  # <1>
    def __prepare__(meta_cls, cls_name, bases):  # <2>
        args = (meta_cls, cls_name, bases)
        print(f'% MetaKlass.__prepare__{args!r}')
        return NosyDict()  # <3>返回一个命名表空间字典。这里为了后面打印看到命名的过程，定制了一个UserDict来返回。

    def __new__(meta_cls, cls_name, bases, cls_dict):  # <4>cls_dict是NosyDict() 的实例
        args = (meta_cls, cls_name, bases, cls_dict)
        print(f'% MetaKlass.__new__{args!r}')

        # <5>type.__new__的最后一个参数必须是真正的字典，而不是实例，所以传入NosyDict从UserDict继承的data属性
        cls = super().__new__(meta_cls, cls_name, bases, cls_dict.data)

        # 在type.__new__结束后，对返回的新类再次注入一个新的方法
        def inner_2(self):
            print(f'% MetaKlass.__new__:inner_2({self!r})')
        cls.method_c = inner_2  # <6>

        return cls  # <7>

    def __repr__(cls):  # <8>
        cls_name = cls.__name__
        return f"<class {cls_name!r} built by MetaKlass>"


print('% metalib module end')
# end::METALIB_BOTTOM[]
