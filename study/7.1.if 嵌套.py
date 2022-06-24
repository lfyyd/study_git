# 嵌套
# n = 11
# m = 5
# if m > 3:
#     print('1111111')
#     if n < 10:
#         print('9<10')
#     else:
#         print('不是9<10')
#     print('22222')
# else:
#     print('33333')

'''
键盘上输入以下内容并打印输出：
默认（admin，1234）
用户名：username
密码：password
是否记住密码bool类型，is_remember

如果用户名和密码正确并且 is_remember是True表示记住密码，则打印已经记住用户xxx的密码啦
否则打印，没有记住密码需要下次继续输入的：
'''
name = '凉风'
result1 = input('请输入username:')
result2 = input('请输入password:')
is_remember = True

if result1 == 'admin' and result2 == '1234':
    if is_remember:
        print('已经记住用户%s的密码啦' % name)
    else:
        print('没有记住密码需要下次继续输入的：')
else:
    print('用户名或密码错误')
