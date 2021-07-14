# 未定参数个数


# a有若干个参数
# 将所有参数视为一个tuple
def a(*args):
    print(args)
    for r in args:
        print(r)


a(1, 'a')
a(True, None, [3, 2, 1])
print()


# b参数是x=y形式，也是若干个
# 将所有参数视为一个dictionary
def b(**kwargs):
    print(kwargs)
    for r in kwargs:
        print(r)


b(x=True, y=None, z=[3, 2, 1])
print()


def u(x, y, z, *args, **kwargs):
    w = x + y ** z
    print(w)
    print(args)
    print(kwargs)
u(9,3,7,1,{'hk':'free','ch':3},0,(None,'abcde'),a=1111,b=2222)