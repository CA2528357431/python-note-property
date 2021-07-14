# 装饰器 参数

def check(func):
    print('front') # 此层的内容在程序最开始就执行
    def doin(y):
        x = int(input('check  ')) # 此层的内容在调用的时候执行
        if x == 0:
            print('good')
        else:
            print('bad')
        func(y)

    return doin


@check  # 修饰
def do(y):
    print('hk free\n'*y)

# 调用
do(3)
