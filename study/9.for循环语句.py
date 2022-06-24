"""
for (。。。) {
     循环体
}

格式：
for n in range（n）：
      循环体中的内容

range（n） ：默认从0开始取值到h-1结束
range（start，stop）：【start，stop】
"""
# while的方式打印1-10 数字打印
# n = 0
# while n < 10:
#     n += 1
#     print(n)

# 打印 1-10 数字打印

# for n in range(5, 10):
#     print(n)
#
# print('*' * 20)

# for i in range(5,10):
#     print('---->',i)

# for i in range(1,10,2):
#     print('---->',i)

# 1-50的 累加和  while 和 for的区别
# n = 0
# i = 0
# while n <= 49:
#     n += 1
#     i += n
#     print(i)

# n = 0
# for i in range(0, 51):
#     n += i
#     print(n)
'''
输入用户名和面膜，如果三次都没有登录成功，提示账号被锁定
'''
# count = 0
# for i in range(1,3):
#     zh = input('请输入账号:')
#     mm = input('请输入密码:')
#     if zh == 'admin' and mm == "123456":
#         print('登录成功')
#         break
#     elif zh != 'admin' or mm != "123456":
#         count += 1
#         if count == 3:
#             print('账号被锁定')
#             break
#         else:
#             print('账号密码错误')

"""
fro ...else
if 条件：
    pass
else：
    pass

for i in range(n):
    循环体
else：
    循环体从头执行到完，没有报错才会执行到这个

"""
# for i in range(1, 4):
#     zh = input('请输入账号:')
#     mm = input('请输入密码:')
#     if zh == 'admin' and mm == "123456":
#         print('登录成功')
#         break
#     else:
#         print('账号密码错误')
# else:
#     print('账号被锁定')

"""
这个时候 思考会不会有while。。。else,?   答案：一样有的，else 可以使用的
"""
# n = 1
# while n <= 5:
#     print(n)
#     n += 1
# else:
#     print('有else吗？')


'''
-----------------------------------for循环和 while 循环的区别以及运用---------------------------- 
for i in range(n):----->肯定是有固定次数的
     pass
while 条件： -----》固定次数  2，不确定次数的循环
     pass
    
不确定次数的循环 
while True:
     pass
'''

# 练习

'''
投骰子
两个：1-6
1. 玩游戏要有金币，没金币不能玩游戏
2. 玩游戏赠金币1枚，或者充值获取金币
3. 10元的倍数才能充值，充10个得20个金币
4. 玩一局游戏消耗5个金币
5. 猜大小: 猜对 有鼓励金币2枚， 错没有   超出6点以上认为是大，否则是小
6. 游戏结束: 1.主动退出 2.没有金币退出
7. 只要退出则打印金币数，共玩了几局
'''

# 自己写的
import random
money = 0
jiju = 0
while True:
    if money >= 5:
        sz1 = random.randint(1, 6)
        sz2 = random.randint(1, 6)
        zh = sz1 + sz2
        print(zh)
        guess = int(input('请输入2-12数字:'))
        if guess > zh:
            jiju += 1
            money -= 5  # 玩游戏消耗5个金币
            money += 2  # 猜对了赠送2个金币
            money += 1  # 玩游戏赠送一个金币
            print('猜对了大')
            if money == 0:
                break
            jx = input('是否要继续游戏还是退出(y/n)')
            if jx == 'n':
                print('现有金额:%s,共玩了%s局游戏'%(money,jiju))
                break
        elif guess == zh:
            print('本局平局')
        else:
            jiju += 1
            money -= 5
            money += 1
            print('猜错了小')
            if money == 0:
                break
            jx = input('是否要继续游戏还是退出(y/n)')
            if jx == 'n':
                print('现有金额:%s,共玩了%s局游戏' % (money, jiju))
                break
    elif 0 <= money < 5:
        cz = input('金币不足是否要充值(y/n):')
        if cz == 'y':
            je = int(input('请输入10位整数充值金额:'))
            if je % 10 == 0:
                je1 = je *2
                money += je1
                print(money)
            else:
                print('输入错误，请输入10整数或倍数')
        elif cz =='n':
            break

# 教程写法
# import random
# coins = 0
# count = 0
# if coins < 5:
#     # 提示充值
#     print('金币不足请充值再玩!')
#     while True:
#         money = int(input('请输入充值金额:'))
#         # 10的倍数，20金币
#         if money % 10 == 0:
#             coins += money // 10 * 20
#             print('充值成功! 现金币有%d个' % coins)
#             answer = input('是否开启游戏(y/n)?')
#             # 开启游戏之旅
#             print('~~~~~~~~~~~开始游戏之旅~~~~~~~~~~~~~~~~')
#             while coins > 5 and answer == 'y':
#                 # 扣金币
#                 money -= 5
#                 money += 1
#                 # 产生两枚随机数骰子
#                 ran1 = random.randint(1, 6)
#                 ran2 = random.randint(1, 6)
#                 # 猜大小
#                 guess = input('洗牌完毕，请猜大小:')
#                 # 判断比较
#                 if guess == '大' and ran1 + ran2 > 6 or guess == '小' and ran1 + ran2 < 6:
#                     print('恭喜猜对了，你赢了')
#                     coins += 2
#                 else:
#                     print('本次猜错了')
#                 count += 1
#                 answer = input('是否继续游戏(y/n)?')
#             print('共玩了%d次,剩余金币:%d' % (count,coins))
#             break
#         else:
#             print('不是10的倍数，充值失败!')

