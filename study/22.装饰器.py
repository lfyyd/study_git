'''
   装饰器是装饰用的函数，参数是被装饰的函数在被装饰器装饰之后，多了一点功能或者改变了一些功能
   就是原有函数不改变，加个装饰器，在装饰器内放上自定义名字的必须参数，然后去实例化=必须参数，在实例化的对象
   上面进行添加功能，必须参数就是要被装饰的函数
'''

import time


# 定义一个装饰器函数
def sayLocal(func):
    def wrapper():
        curTime = func()
        return f'当地时间： {curTime}'

    return wrapper


def getXXXTime():
    return time.strftime('%Y_%m_%d %H:%M:%S', time.localtime())

sayLocal(getXXXTime)
print(sayLocal(getXXXTime))
# print(getXXXTime())
# # 装饰 getXXXTime
# aa = sayLocal(getXXXTime)
# print(aa())

# Python 中 对应第14行代码， 可以有更方便的写法，如下

# import time
#
# def sayLocal(func):
#     def wrapper():
#         curTime = func()
#         return f'当地时间： {curTime}'
#     return wrapper
#
# @sayLocal
# def getXXXTime():
#     return time.strftime('%Y_%m_%d %H:%M:%S',time.localtime())
#
# print (getXXXTime())
