# 装饰器

# 需求是在不改变do函数的前提下添加一个验证input的功能

# 完成修饰内容
def check(func):
    def doin():
        x = int(input('check  '))
        if x == 0:
            print('good')
        else:
            print('bad')
        func()

    return doin


@check  # 修饰
def do():
    print('hk free')


# 调用
do()

# 调用的其实是doin，只是将do这个指针重定向到了doin
