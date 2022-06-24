'''
try 下面缩进的3行代码可以看成是 保护区 中的代码。
如果执行保护区中代码时，出现异常，解释器会结束保护区中后续代码的执行，并检查这个异常的类型是否匹配后面的except 语句中声明的类型。
如果匹配上，解释器知道程序对此种异常是预料到的，并且有对应的处理方案，也就是匹配的except下面缩进的代码。解释器就执行匹配的except下面缩进的代码，不会因此中止程序。
'''
# result = True
# while result:
#     try:
#         miles = input('请输入英里数:')
#         km = int(miles) * 1.609344
#         print(f'等于{km}公里')
#         result = False
#     except ValueError:
#         print('你输入了非数字字符')


'''
捕获所有的异常 可以用 Exception，因为它是所有异常的父类。  也可以什么都不填默认捕获所有
'''
#
# try:
#     100/0
# except Exception as e:
#     print('未知异常:', e)
#
#
# try:
#     100/0
# except:
#     print('未知异常')

'''
如果我们想知道异常的详细信息，可以使用traceback模块，如下，
'''
# import traceback
#
# try:
#     100/0
# except :
#     print('异常',traceback.format_exc())


'''
自定义异常
'''

# 异常对象，代表电话号码有非法字符
# class InvalidCharError(Exception):
#     pass
#
# # 异常对象，代表电话号码非中国号码
# class NotChinaTelError(Exception):
#     pass
#
#
# def register():
#     tel = input('请注册您的电话号码:')
#
#     # 如果有非数字字符
#     if not tel.isdigit():
#         raise InvalidCharError()
#
#     # 如果不是以86开头，则不是中国号码
#     if not tel.startswith('86'):
#         raise NotChinaTelError()
#
#     return tel
#
# #
# # try:
# ret = register()
# except InvalidCharError:
#     print('电话号码中有错误的字符')
# except NotChinaTelError:
#     print('非中国手机号码')

# import traceback
# while True:
#     try:
#         result = int(input('输入:'))
#     except:
#         print('输入错误了',traceback.format_exc())
#


#