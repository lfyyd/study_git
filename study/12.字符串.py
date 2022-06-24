# 字符串

# s1 = 'hello'
# s2 = s1
# s3 = 'hello'
# s4 = 'haha'
#
# print(s1,s2,s3)
#
# print(id(s1))
# print(id(s2))
# print(id(s3))
# print(id(s4))
#
# # is  地址比较的
# print(s1 is s4)

# s1="ABCDEF"
# print(s1[5])
# print(s1[0])
#
# print(s1[-1],s1[5])
# print(len(s1))  # len通过len算出字符串有多少个


"""
切片:列表，字符串
格式: 字符串变量[start:end]
"""

# s = 'abcdefg'
# print(s[1:4])  # bcd
# print(s[0:6])
# print(s[:5])  # 从0到5
# print(s[-3:])  # 从-3开始到结尾
# print(id(s[:]))  # 从头到位
# print(id(s))  # 内容一样 id地址是一样的
#
# print(s[1:6])
# print(s[1:-1])
#
# print('*-' * 20)
# print(s[:-1:2])
# print(s[1::2])
import random

"""
https://www.baidu.com/?tn=49055317_36_hao_pg
find: 从左向右查找，只要遇见一个符合要求的位置。  如果没有找到符合要求的则返回-1
rfind: 从右往左查找，找到第一个位置符合要求的位置。
conut: 统计指定字符的个数
"""

# path = 'https://www.baidu.com/?tn=49055317_36_hao_pg'
#
# # find查找
# i = path.find('h')
# print(i)
# image_name = path[i+1:]
# print(image_name)
#
# # rfind 查找
#
# i = path.rfind('.')
# print(i)
# zhui = path[i:]
# print(zhui)
#
# '''
# 查找字符串中有几个。？
# '''
# n = path.count(".")
# print(n)

'''
判断： startswith.endswith.isdigit.isalnum.isspace
返回的都是布尔类型（True,False）
'''

# a = 'tn=49055317_36_hao_pg'
# result = a.startswith('tn')   # 判断是否以xx开头
# print(result)
#
# result1 = a.endswith('pg')  # 判断是否以xx结尾
# print(result1)


'''
模拟文件上传，键盘输入上传文件的名称，判断文件名是否大于6位数以上，拓展名是否是:jpg,gif,png格式
如果不是则提示上传失败，如果名字不满足条件，而拓展名满足条件则随机生成一个6位数字组成的文件名，打印成功上传该名字文件
'''
# import random
#
# wj = input('请输入上传文件名称:')
# tj = len(wj)
# dtj = tj - 4
# result = wj.endswith('jpg')
# result1 = wj.endswith('gif')
# result2 = wj.endswith('png')
# if result == True or result1 == True or result2 == True:
#     if dtj == 6:
#         print('上传成功')
#     elif dtj > 6:
#         parse = str(random.randint(100000, 999999))
#         pa = (wj[-4:])
#         par = parse + pa
#         print(par)
#         print('上传%s文件成功' % par)
#     else:
#         parse = str(random.randint(100000, 999999))
#         pa = (wj[-4:])
#         par = parse + pa
#         print(par)
#         print('上传%s文件成功' % par)
# else:
#     print('上传失败')


# 字母和数字的组合
# import random
# lenname = ''
# s = 'abcderg'
# for i in range(6):
#     index = random.randint(0,len(s)-1) # 0
#     lenname += s[index]
# print(lenname)


# s = 'aaaa'
# result = s.isalpha()  # 判断全部是否是字母
# print(result)
#
# s = '123'
# result = s.isdigit()  # 判断全部是否是数字
# print(result)
#
# s = 'a1234'
# result = s.isalnum()  # 判断全部是字符串，有特色符号就是False
# print(result)
#
# s = '    '
# result = s.isspace()  # 判断是否是一个空字符串，不是空的为False
# print(result)
#
# s = 'AAAA'
# result = s.isupper()  # 判断是否是大写的
# print(result)
#
# result = s.islower()  # 判断是否是小写的
# print(result)

# flag = True
# while flag:
#     name = input('用户名/手机号码:')
#     if (name.islower() and name[0].isalpha() and len(name) > 6) \
#             or (name.isdigit() and  len(name) == 11):
#         while flag:
#             password = input('请输入密码:')
#             if password.isdigit() and len(password) == 6:
#                 if password == '123456' and name == 'admin123' or name == '17610372399':
#                     print('登录成功')
#                     flag = False
#                 else:
#                     print('账号或者密码错误!')
#                     break
#             else:
#                 print('密码必须是6位数字')
#     else:
#         print('用户名或者手机号码格式错误!')
#


'''
空格处理:
ljust.rjust.center    添加空格控制字符串的对齐方式
lstrip，rstrip，strip  删除空格左边右边，中间的空格

字符串拼接: join
'''
#
# username = input('用户名:') # admin
# print(len(username))

# admin  admin  admin

# s= ' admin '
# print(len(s))
# result = s.strip() # strip把两边的空格删除掉
# print(len(result))
#
# result = s.lstrip() # lstrip把最左侧的空格删除掉
# print(len(result))
#
# reuslt = s.rstrip() # rstrip把最右侧的空格删除掉
# print(len(result))
#
# s = 'hello world'
# result = s.center(30) # 加空格把字符放中间
# print(result)
#
# result = s.ljust(30)  # 加空格把字符放最左侧
# print(result)
#
# result = s.rjust(30)  # 加空格把字符放最右侧
# print(result)
#
# s = 'hello'+'word'
# print(s)

'''
模拟论坛
昨天晚会遇见一个漂亮的小姐姐，要不要去表白？
输入用户名:凉风
反复回复:
  1.回复的内容不能为空
  2.里面不能带敏感词汇
  3.最多评论20个字，剩余多少个字
  4.回复的内容不能有空格
小白:
   抓紧表白
小黑:
   上啊
小蓝:
   不行我来
'''
# message = input('发表一句话:')
# print('-' * 50)
# print('以下为回复内容:')
# while True:
#



"""
模拟论坛

"""

msg = input('发表一句话:')
print('-'*50)
print('以下为回复的内容')