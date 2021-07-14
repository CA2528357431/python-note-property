# 多重装饰

def add1(fun):
    def in1():
        print(11)
        fun()
        print(1)

    return in1


def add2(fun):
    def in2():
        print(22)
        fun()
        print(2)

    return in2


def add3(fun):
    def in3():
        print(33)
        fun()
        print(3)

    return in3


@add2
@add1
@add3
def fun():
    print('aaaaaaaaaaaaaaa')


fun()

# 本质上是修饰了一个被修饰的函数
# 可以理解为多重修饰是对 修饰函数 的和合并同类项
# 本题中合并后的
#   def add(fun):
#     def in():
#         print(22)
#         print(11)
#         print(33)
#         fun()
#         print(3)
#         print(1)
#         print(2)
#     return in3
# 由 ’内到外‘ 按照 ’靠近被修饰函数‘ 的顺序 ‘包裹’ 被修饰函数
