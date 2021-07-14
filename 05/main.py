# 不定装饰器


def um(func):
    def uin(x, y, z, *args, **kwargs):
        r = int(input('check  '))
        if r == 0:
            print('good')
        else:
            print('bad')
        func(x, y, z, *args, **kwargs)

    return uin


@um
def u(x, y, z, *args, **kwargs):
    w = x + y ** z
    print(w)
    print(args)
    print(kwargs)


u(7, 3, 9, [1, 'a', None], True, r=None, b=0)
