"""
循环退出语句：
1.break
2.continue

都是出现在循环中

不同：
break 跳出循环结构
conuinue  跳出本次循环（后面的语句不执行了）继续下一次循环
"""

# 不打印能被3整除的
# for i in range(10):
#     if i % 3 != 0:
#         print(i)

# for i in range(10):
#     if i % 3 != 0:
#         continue  # 当判断达成，运行conuinue，它的下方都不执行
#         print(i)
#         print('你好')
#         print('你好')
#     print(i)

"""
循环嵌套：
if 条件:
    if  条件:
        pass
else:
    if  条件:
        pass 
"""

"""
while循环:
*
**
***
****
*****
"""
# n = 1
# while n <= 4:
#     print('*'*n)
#     n += 1

# for i in range(1, 6):
#     print('*' * i)

# n = 1
# while n <= 5:
#     m = 0
#     while m < n:
#         print('*',end="")
#         m += 1
#     n += 1
#     print()

'''
*****
****
***
**
*

'''
# n = 5
# while 0 < n <= 5:
#     m = 0
#     while m < n:
#         print('*', end="")
#         m += 1
#     n -= 1
#     print()
'''
打印99乘法表
'''
for a in range(1, 10):
    for b in range(a):
        print(f'{b + 1}x{a}={(b + 1) * a}', end=' ')
    print()

# j = 0
# while j < 9:
#     j += 1
#     i = 0
#     while i < j:
#         i += 1
#         print(i, '*', j, '=', (i * j),sep='', end='\t')
#     print()