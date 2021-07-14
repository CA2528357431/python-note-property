#  装饰器中添加参数

def arg(a, b, c):
    def check(func):
        def doin():

            x = int(input('check  '))
            if x == 0:
                print('good')
            else:
                print('bad')
            z = a ** b + c
            print(z)
            func()

        return doin

    return check


a = int(input('a '))
b = int(input('b '))
c = int(input('c '))


@arg(a, b, c)
def do():
    print('hk free')


do()
