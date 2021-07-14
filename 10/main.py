# 类修饰器

def do(cla):
    def inner(a, b, c):
        print('Tora Tora Tora')
        obj = cla(a, b, c)
        obj()
        return obj

    return inner


@do
class bate:
    def __init__(self, a, b, c):
        self.id = a
        self.age = b
        self.hope = c
        print('success')

    def __call__(self):
        print('cooooooooooool')


ex = bate(1, 1, 1)
# 在创建对象时在__init__之前自动调用
# 可以借此来完成单例
