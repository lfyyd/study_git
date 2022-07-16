# 内部函数
'''
特点：
1.可以访问外部函数的变量
2.内部函数可以修改外部函数的可变类型的变量比如list1
3.内部函数修改全局的不可变变量时，需要在内部函数声明: global 变量名
  内部函数修改外部函数的不可变变量时，需要在内部函数中声明:  nonlocal 变量名

'''

a = 50


# 外部函数
def func():
    global a
    n = 100  # 外部变量
    list1 = [5, 2, 9, 4, 1]  # 外部变量

    # 内部函数
    def inner_func():
        global a
        nonlocal n
        list1.sort()  # 调用了外部变量list1
        n += 5  # 修改外部函数的不可变变量
        a -= 5  # 修改全局的不可变变量

    inner_func()  # 在外部函数调用内部函数
    a -= 5
    print(list1, n, a)
    # print(locals())
    # print(globals())


func()

'''
闭包函数
条件：
1.外部函数中定义了内部函数
2.外部函数是有返回值的
3.返回的值是 内部函数名
4.内部函数引用了外部函数的变量

格式：
def 外部函数（）：
    pass
    def 内部函数（）：
        pass
    return 内部函数

'''


# 闭包
# 外部函数
def func(a, b):
    c = 10

    # 内部函数
    def inner_func():
        s = a + b + c
        print(s)

    return inner_func  # 把内部函数整个返回给外部函数


x = func(1, 2)  # 把内部函数赋值给变量，x就等于内部函数inner_func()
x()  # 然后调用函数就可以了

'''
闭包有什么缺点呢？
闭包的缺点1：作用域没有那么直观
闭关的缺点2：因为变量不会被垃圾回收所有有一定的内存占用问题

闭包的作用：
1.可以使用统计的作用域
2.读取其他元素的内部变量
3.延长作用域

闭包总结：
1.闭包似优化了变量，原来需要类对象完成的工作，闭包也可以完成
2.由于闭包引用了外部函数的局部变量，则外部函数的局部变量没有及时释放，消耗内存
3.闭包的好处，使代码变得简洁，便于阅读代码
4.闭包是理解装饰器的基础

'''


def function():
    a = 100

    def inner_function1():
        b = 90
        s = a + b
        print(s)

    def inner_function2():
        inner_function1()  # 闭包同级调用
        print('----->inner_function2')

    return inner_function2()


function()


# 计数器
def count():
    counts = [0] # 这个和while 循环一样是个计数器

    def add_one():
        counts[0] += 1
        print('当前是第{}次访问'.format(counts[0]))

    return add_one

# 内部函数就是一个技术器
counter = count()

counter()
counter()
counter()
