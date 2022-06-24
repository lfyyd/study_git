# print('hello word')
# name = '李泽'
# print(name)

# input()

# uesrName = input('请输入用户名:')  # 阻塞
#
# print('哈哈哈')
# print(uesrName)
# print(type(uesrName))
#
# money = input('请输入缴费金额:')
# print(money)
# print(type(money))
#
# # print(uesrName+1000)
#
# # 类型转换 str ---》int
# print(int(money) + 1000)

'''
键盘输入两个整数，输出两个整数的和，输入差
input('输入第一个数:')
input('输入第二个数:')

'''

# result = input('请输入第一个数:')
# money = input('请输入第二个数:')
# print(int(result) + int(money))
# print(float(result) + float(money))
# print(int(result) - int(money))
# print(float(result) - float(money))
#
# a=9.9
# print(int(a))
'''
以变量名：a
 str ---》int  int（a)  但是如果‘9.9’而且是字符串类型转成int就会报错
 str --->float float(a)
 
 int ---》str  str(a)
 float --->str  str(a)
 
 int --->float   float(a)
 float --->int  int(a)  只不过float类型中小数点后面的数据被抹掉了
 
'''
# flag = True
# # bool ---》int  True转整型就会是1   False转整型就会是o
# print(int(flag))
# print(float(flag))
# print(str(flag))  # 会是True

'''
思考：
a = 5
能否将a转换成bool类型？

'''

a = 5
print((bool(a)))

a = 0
print((bool(a)))

a = 'nihao'
print((bool(a)))

a = ''
print(bool(a))

# 变量的值是：0，''（空字符串），转换的结果为False，其他只要有变量的就为True
