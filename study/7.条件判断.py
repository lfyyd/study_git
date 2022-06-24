'''
if
if...else
if...elis...else

if语句的格式：
if 条件：
   条件成立要执行的语句

if语句的格式：
if 条件：
   条件成立要执行的语句
else：
   条件不成立要执行的语句

'''
#
# print(1)
# print(2)
# print(3)
#
# # 4,5有条件的打印
# result = input('请输入(y/n):')
# if result == 'y':
#     print(4)
#     print('over~~~~~')
# print('----------------')


# 随机数
import random  # 导入随机数库

# ran = random.randint(1, 10)  # 随机1-10数字
# print(ran)
# result = int(input('请输入你猜的数字:'))
#
# if ran == result:
#     print('恭喜猜对了')
# else:
#     print('恭喜猜错了')

# 输入账号密码，账号为admin，密码为123456，判断输入是否正确？
# username = input('请输入账号:')
# password = input('请输入密码:')
#
# if  username == 'admin' and password == '123456':
#     print('登录成功')
# else:
#     print('登录失败')
#
'''
三判断
if 条件1：
   条件True，执行的语句
elif 条件2：
   条件True，执行的语句
elif 条件3：
   条件True，执行的语句
else：
1，2，3条件都不符合的情况下，才到这个

'''
# 输入销售金额获取礼物
'''
0-1：你真棒
1-5：奖励1000元
5-10：奖励笔记本
10-20：奖励iphone12
超过20万：奖励一个特斯拉
'''

# money = 31
#
# if 0<=money<=1:
#     print('你真棒')
# elif 1<=money<=5:
#     print('奖励1000元')
# elif 5<=money<=10:
#     print('奖励笔记本')
# elif 10<=money<=20:
#     print('奖励iphone12')
# elif 20<money<=30:
#     print('奖励一个特斯拉')
# else:
#     print('二鑫一个')

# 判断成绩为80分以上的就是优秀，其他的是一般
# chengji = int(input('请输入成绩:'))
# if chengji > 80:
#     print('优秀')
# else:
#     print('一般')

# 判断成绩80以上的评级优秀，60以下的评级不及格，其他一般
# chengji = int(input('请输入成绩:'))
# if chengji >= 80:
#     print('优秀')
# elif 60<chengji<80:
#     print('一般')
# else:
#     print('不及格')

'''
人员管理系统，功能:  添加员工  删除员工  查询员工  修改员工信息

'''

# print('--------欢迎进入人员管理系统--------')
# choice = int(input('请选择功能: \n 1.添加员工 \n 2.删除员工 \n 3.查询员工 \n 4.修改员工信息'))
# if choice == 1:
#      print('添加员工')
# elif choice == 2:
#      print('删除员工')
# elif choice == 3:
#      print('查询员工')
# elif choice == 4:
#      print('修改员工信息')
# else:
#      print('输入错误请重新输入')


'''
阿里爸爸商家节，用户名，消费总金额，账户金额，优惠券
输入购买总购买金额：
如果金额0-500则是lv1级别
如果500-2000元则是lv2级别
其他的则为lv3级别

lv1：随机赠送3张1-10元的优惠券
lv2：赠送2张50元优惠券，如果充值则送充值金额的10%
lv3：赠送2张100元优惠券，如果充值则赠送15%的金额
'''
# import random
#
# username = '梁枫'
# total = 1900  # 消费总金额
# money = 0  # 账户金额
# coupon = 0  # 优惠券
#
# # 根据总金额判断级别
# if 0 < total < 500:  # lv1
#     # 随机赠送3张1-10元的优惠券
#     quan1 = random.randint(1, 10)
#     quan2 = random.randint(1, 10)
#     quan3 = random.randint(1, 10)
#     # 将金额数加到coupon
#     coupon = quan1 + quan2 + quan3
# elif 500 <= total < 2000:  # lv2
#     # 赠送2张50元优惠券，如果充值则送充值金额的10%
#     coupon += 2 * 50
#     # 嵌套if
#     recharge = input('%S,是否要充值(送充值金额的10%)？(y/n)')
#     if recharge == 'y':
#         money += 1.1 * int(input('输入充值金额:'))
#     print(money)
# elif total >= 2000:  # lv3
#     # 赠送2张100元优惠券，如果充值则赠送15%的金额
#     coupon += 2 * 100
#     recharge = input('%S,是否要充值(送充值金额的15%)？(y/n)')
#     if recharge == 'y':
#         money += 1.5 * int(input('输入充值金额:'))
#     print(money)


"""
1.关系运算符
键盘输入年龄，判断年龄是否大于等于18岁
键盘输入两个年龄，小明小芳年龄，判断两者的年龄是否相同
键盘上输入两个人的姓名，判断是否相同

"""
# result = int(input('请输入年龄:'))
# print(result >= 18)
# result1 = int(input('请输入小明的年龄:'))
# result2 = int(input('请输入小芳的年龄:'))
# if result1 == result2:
#     print('年龄相同')
# else:
#     print('年龄不相同')
# result3 = input('请输入姓名:')
# result4 = input('请输入姓名:')
# if result3 == result4:
#     print('姓名相同')
# else:
#     print('姓名不相同')

"""
2.键盘上输入以下内容并打印输入：
默认（admin，1234）
用户名，username
密码，password
是否记住密码bool类型，is_remember

如果用户名和密码正确并且is_remember是True，表示记住密码，则打印已经记住用户xxx的密码了
否则打印，没有记住密码需要下次继续输入
"""
# name = '梁枫'
# parse = input('请输入username:')
# parse1 = int(input('请输入password:'))
# is_remember = True
#
# if parse == 'admin' and parse1 == 1234:
#     print('%s登录成功'%name)
# elif parse == 'admin' and parse1 != 1234:
#     print('%s密码错误'%name)
# elif parse != 'admin' and parse1 == 1234:
#     print('%s账号错误'%name)
#

'''
3.键盘上输入你的身高和体重并打印输入
BMI = 体重（公斤）/身高（米）的平方
如果小于18.5，随便吃
如果18.5-23.9真是好身材
如果是23.9-27 管好嘴巴把，再吃成胖子了
如果大于27 随便把就这样了
'''
# random1 = float(input('请输入身高(1.x）:'))
# random2 = int(input('请输入体重:'))
# BMI = random2 / (random1 ** 2)
# print(BMI)
# if BMI < 18.5:
#     print('随便吃')
# elif 18.5 <= BMI < 23.9:
#     print('真是好身材')
# elif 23.9 <= BMI <= 27:
#     print('管好嘴巴把，再吃成胖子了')
# else:
#     print('随便把就这样了')
'''
4.假如登录途牛网站，买票
可以通过账号登录
也可以通过手机号码登录+密码
账户：lf123456
密码：123456 手机号17610372388
判断是否登录成功

'''
# match = input('请输入账号:')
# match1 = int(input('请输入密码或手机号:'))
#
# if match == 'lf123456' and match1 == 123456 or match1 == 17610372388:
#     print('登录成功')
# else:
#     print('登录失败')
'''
求给定的年份，是否为闰年，键盘输入一个年份
满足以下两点中任意一点就是闰年
A；能被4正除，但是被100整除
B：能被400整除

'''
# result = float(input('请输入年份:'))
#
# if 4 // result and 100 // result or 400 // result:
#     print('闰年')
# else:
#     print('不是闰年')

'''
键盘上输入1-5个数字，分别代表
1.特遣队列表
2.添加特遣队列表
3.删除特遣队列表
4.修改特遣队列表
5.退出

以下选做：
'''
# number = int(input('\n1.特遣队列表 \n2.添加特遣队列表 \n3.删除特遣队列表 \n4.修改特遣队列表 \n5.退出 \n请输入:'))
# if number == 1:
#     print('特遣队列表')
# elif number == 2:
#     print('添加特遣队列表')
# elif number == 3:
#     print('删除特遣队列表')
# elif number == 4:
#     print('修改特遣队列表')
# elif number == 5:
#     print('退出')
# else:
#     print('输入错误')

"""
模拟超市付款： 商品单价 商品数量
   键盘上输入商品单价，以及商品数量，然后计算应付总额
提示用户可以有4种付款方式
不同的付款方式有不同的折扣，先展示四种付款方式
现金没有折扣
微信 0.95折
支付宝  鼓励金付款金额的10%，鼓励金可以直接折算到付款金额中
刷卡 满100-20
"""

print('-----欢迎来到枫谷超市------')
result = float(input('请输入商品单价:'))
result1 = int(input('请输入商品数量:'))
match = result * result1  # 应付总额
# print(match)
# 四种付款方式
match1 = int(input(' 1.现金交易\n 2.微信交易\n 3.支付宝交易\n 4.刷卡交易\n 请选择交易方式:'))

if match1 == 4:
    if match >= 100:
        match -= 20
        print('刷卡 满100-20')
    else:
        print('未达到金额没有优惠')
elif match1 == 1:
    print('没有折扣')
elif match1 == 2:
    match = match * 0.95
    print('微信支付0.95折')
elif match1 == 3:
    money = match * 0.1
    match -= money
    print('鼓励金付款金额的10%，鼓励金可以直接折算到付款金额中')
else:
    print('输入错误')
print(match)

