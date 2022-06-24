'''
= 赋值运算符
算术运算符：+，-，*，/，%，//，，**

'''

# a = 1
# b = 2
#
# c = a + b
# print(c)
# print(a, b, c, 100, 1000, sep='#')  # sep 分割符
# print(a, b, c, end='')   # end='' 末尾换行
# print(a, b, c)
#
# print(c - a)
#
# print(c * a)
#
# print(c / 2)  # 除法
# print(c // 2)  # 整除
#
# print(2 ** 3)  # m ** n 表示m的n次方
#
# # 取模 去余
# print(3 % 2)  # 奇数 偶数

'''
键盘输入一个三位数的整数，打印个位数，十位数，百位数
'''
#
# parse = int(input('请输入三位的整数:'))
# print('个位数:', parse % 10)
# print('十位数:', parse // 10 % 10)
# print('百位数:', parse // 100 % 10)
# print('千位数:', parse // 1000 % 10)
#
# a = 2298
# b = 1000
# print(a // b % 10)

# a = 8
# b = 4
# c = a + 1
#
# a += 1 #a=a+1
# print(a, b, c)
#
# a += b #a=a+b
# print(a,b,c)
#
# b-=2
# print(a,b)
#
# d=3
# b//=d #b=b//d
# print(a,b,c,d)

'''
关系，比较运算符： 结果：True False
> < >=  <= == != is


'''
# a = 10
# b = 23
# print(a > b)  # False
# print(a < b)  # True
#
# print(a == b)  # False
#
# print(a != b)  # True
#
# x = 'abc'
# y = 'abd'
# print(x == y)  # False
# print(x < y)  # True
# # 字符串按a，b，c，d以此对比比较，按字符顺序比较，a比b小，这样往后算
#
# c = 10
# print(a >= c)  # True

'''
输入考试分数，判断成绩是否在100到80之间？

'''
# parse = float(input('请输入成绩:'))
# print(80 <= parse <= 100)

'''
输入hauwei mate40 价格：
输入iphone 12 价格：
判断是否价格相等
'''
# match = int(input('请输入hauwei mate40 价格:'))
# result = int(input('请输入iphone 12 价格:'))
# print(match == result)

'''
逻辑运算符:
and or not

结果: 
and: 与  并且  两边有一个为False 结果即为False,如果and两边为Ture，取最后一个值
 A and B
 Ture and Ture --->Ture
 Ture and False --->False
 False and Ture --->False
 False and False --->False
 
or : 或 或者 只要有一侧有True 结果即为Ture
 
not:
not Ture --->False
not False --->Ture

'''

a = 3
b = 1

print(a and b)
# 如果两次都是数字，且都是非0的，取后面的数字值
c = 0
print(a and c)
# and两边只有一边有0，那么结果即为0

print(a > c and a > b)  # username == ‘小花’ and password == '123456'
print(a == c and a < b)

print('*' * 20)
print(b or a)
print(a or c)

print(a < b and a > b)
print(a < b or a > b)  # 场景： 1，账号密码 or 手机号码 验证码

print('-*' * 20)
flag = True
print(not flag)

print(not a>c)

