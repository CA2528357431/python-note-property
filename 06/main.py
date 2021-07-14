# 装饰器 返回

def uu(fun):
    def uin(a,b,c):
        x=int(input('check  '))
        if x==0:
            print('yes')
        else:
            print('no')
        return  fun(a,b,c)
    return uin


@uu
def u(a,b,c):
    z=a+b+c
    print('do',z)
    return z+100000


re=u(3,9,7)
print('result : ',re)