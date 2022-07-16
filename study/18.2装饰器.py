# 装饰器
'''
 加入购物车，付款，修改收货地址....
 判断用户的登录状态


'''

# def func(number):
#     a = 100
#
#     def inner_func():
#         nonlocal a
#         nonlocal number
#         number += 1
#         for i in range(number):
#             a += 1
#
#         print('修改后的a:', a)
#
#     return inner_func
#
#
# # 调用func
# x = func(5)
# x()
#
# # 函数作为参数
# a = 50
# x1 = func(a)  # a是一个实参
# x1()


# 地址引用
# a1 = 10  # 声明整型变量
# b = a1
#
#
# def Test():  # 声明函数
#     print('---------test---------')
#
#
# # t = Test
# # Test() # 一个地址 <function Test at 0x0000018B46F371F0>
# # t()    # 一个地址 <function Test at 0x0000018B46F371F0>
#
# def func(f):
#     print(f) # <function Test at 0x0000018B46F371F0>
#     f()   # ---------test---------
#     print ('---------func---------')
#
#
# func(Test)
from time import sleep

'''
特点:
1.函数A是作为参数出现的,函数B就接受函数A作为参数
2.要有闭包的特点
'''


# 定义一个装饰器
def decorate(func):
    a = 100
    print('wrapper外层打印测试')

    def wrapper():
        func()
        print('-----刷漆')
        print('-----铺地板', a)
        print('-----装修')

    print('wrapper加载完成')
    return wrapper


# 使用定义的装饰器
'''
1.house被装饰函数
2.将被装饰的函数作为参数传给装饰器decorate
3.执行decorate函数
'''


#
# @decorate
# def house():
#     print('我是毛坯房....')


# def house1():
#     house()
#     print('刷漆')
#     print('装修')
#
#
# # 调用函数house
# house()


# 登录校验


def decorate(func):
    def wrapper():
        print('--正在校验--')
        sleep(2)
        print('--校验正常--')
        # 调用原函数
        func()

    return wrapper


@decorate
def f1():
    print('---f1---')


@decorate
def f2():
    print('---f2---')


f1()
f2()
