'''
函数是组织好的,可以重复使用的,用来实现单一或相关的代码
自己创建的函数叫自定义函数
'''


# 定义一个函数:用来比大小,然后将数值大的返回
def bdx(a, b):
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return 0


results = bdx(a=12, b=13)
# results = bdx(12,13)
print(results)
'''
参数的传递:
形式参数:在定义函数时,函数后面括号中的参数就是形式参数
实际参数:就是在调用函数时,函数名后面的括号中的参数称为实际参数
'''

'''
值传递,引用传递
值传递 : 适用于不可变数据类型,  字符串 ,数字, 元祖
通过函数体后不能被修改函数外的值

引用传递 : 使用于可变数据类型, 列表  字典 
通过函数体可以改变函数外变量的值
'''

list1 = [1, 2, 3, 4]


def chengge(list):
    list1.append(list)


print(list1)
chengge([2, 3, 4, 5])
print(list1)

'''
参数类型:
必须参数,关键字参数,默认参数,不定长参数
'''


# 1.必须参数.    必须参数已正确的顺序传入参数,调用时,参数数量必须和申明的一样

def function(mc1, mc2):
    print(mc1, mc2)


function('你好', '靓妹')


# 2.关键字参数  它可以不按顺序去输入参数,必须参数输入的时候是有顺序的,而这个可以用关键字去传
# 时一个特殊的必须参数,它可以通过关键字传值
def aa(bb, cc):
    print(bb, cc)


aa(bb='你好', cc='哈哈')


# 3.默认值传参   如果有默认值，再传入一个新的cc 就会覆盖到默认值的cc 梁枫
def aa(bb, cc='梁枫'):
    print(bb, cc)


aa(bb='nihao')


# 4.不定长参数
# 在定义的过程中，不确定有多少个参数要传，就设置成不定长参数
# 可以在参数前面加一个*或者两个*，就设置成不定长参数了
# 1.参数前面加一个*，把参数存在元祖里面，可以通过切片调用元祖内的元素参数

def a(b, *c):
    print(b)
    print(c)


a('张三', '18', '上海')


# 2. 参数前面带两个**，把不确定长度的参数存在在字典里，通过key调用value
def a(name, **gg):
    print(name)
    print(gg)


a('张三', avg='18', dizhi='上海')


# 函数嵌套
# 函数与函数之间可以相互调用
# 调用函数:在定义的过程中调用另一个函数
def a6():
    print('nihao')


def b6():
    print('hellp')
    b6()


a6()


# 定义函数
def a7():
    print('aa')
    def b7():
        print('bb')
    b7()
a7()


# 函数自己调用自己
def a8():
    print('你好')
    a8()
# a8() # 自己调自己会成为死循环，一直自己调自己


# def interview():
#     print("把求职者带到3号会议室")
#     print("请求职者 完成答卷")
#     print("让测试经理来面试 求职者")
#     print("让技术总监面试 求职者")
#
# interview()
