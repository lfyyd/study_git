'''
循环：
场景：
1.用户名和密码，反复输入
2.计算1-100
3.游戏。死了重生
4. 。。。。

方式：
1.while
2.for

while格式：
   要循环执行的代码

布尔类型的条件
'''

# 初始值
# n = 1
# # 结束条件
# while n <= 10:
#     print(n)
#     # 变量要有变化
#     n += 1

"""
打印1-50之间能被3整除的数字
"""
# n = 1
# while n <= 50:
#     if n % 3 == 0:
#         print(n)
#     n += 1

# while n < 50:
#     n += 1
#     if n // 3 * 3 == n:
#         print(n)

'''
打印1-10之间数字的累加和
'''

# n = 1
# sum = 0  #容器 存放和的结果
# while n <= 10:
#     sum += n
#     n += 1
# print(sum)


'''
超市买东西，价格和数量，允许买多件商品
计算所有商品的总额

'''
# count=0
# while True:
#     print('1111111')
#     count += 1
#     if count == 5:
#         break  #当判断count=5时，break代表跳出循环，就会执行break 跳出这个循环了
# print('起飞')

# total = 0
# sl = 0
# while True:
#     # 先买
#     price = float(input('请输入价格:'))
#     number = int(input('请输入数量:'))
#     total += price * number
#     sl += number
#     # 判断是否继续购买
#     answer = input('当前商品总额是%.2f是否继续购买(y/n)' % total)
#     if answer == 'n':
#         # 跳出while循环
#         break
# print('所有商品的总数的:%s 总额是:%.2f' % (sl, total))

"""
产生一个随机数，
可以猜多次，直到猜对为主，如果猜错了适当给出提示，猜大了，还是猜小了
1.统计猜了几次
2.如果1次就中，赶快去买彩票把，运气爆了
  2-5，猜对了，运气还可以哦
  6以上，猜对了，运气一般啊
"""
# import random

# ran = random.randint(1, 50)
# print(ran)
# count = 0
# while True:
#     result = int(input('猜一个1到50之间的数字:'))
#     count += 1
#     print(count)
#     if result == ran:
#         if count == 1:
#             print('赶快去买彩票把，运气爆了')
#         elif 2 <= count <= 5:
#             print('猜对了，运气还可以哦')
#         elif count > 5:
#             print('猜对了，运气一般啊')
#         break
#     elif result > ran:
#         print('猜大了再小一点')
#     else:
#         print('猜小了再大一点')

"""
猜拳游戏： 3局

"""
import random

# n = 1
# count = 0
# counts = 0
# while n <= 3:
#     # 产生一个数字 0 1 2
#     ran = random.randint(0, 2)
#     print(ran)
#     # 键盘输入猜数字
#     guess = int(input('剪刀(0) 石头(1) 布(2) \n请输入:'))
#     if guess == 0 and ran == 2 or guess == 1 and ran == 0 or guess == 2 and ran == 1:
#         print('恭喜赢了')
#         count += 1
#         if count == 2:
#             print('挑战成功')
#             break
#     elif guess == 0 and ran == 1 or guess == 1 and ran == 2 or guess == 2 and ran == 0:
#         print('输了啊')
#         counts += 1
#         if counts == 2:
#             print('挑战失败')
#             break
#     else:
#         print('本轮平局')
#
# print('本局你赢%s次' % count)
# print('本局代码赢%s次' % counts)


# 输入用户名和面膜，如果三次都没有登录成功，提示账号被锁定

count = 0
while True:
    zh = input('请输入账号:')
    mm = input('请输入密码:')
    if zh == 'admin' and mm == '123456':
        print('登录成功')
        break
    elif zh != 'admin' or mm != '123456':
        count += 1
        if count == 3:
            print('账号被锁定')
            break
        else:
            print('账号密码错误')
