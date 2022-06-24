'''
变量：'容器'
弱语言：变量声明的时候对数据类型不是很严格
java： int a=100
        float b=9.9
python: a=100
1.怎么起名？
2.可以赋什么值
3.有哪些数据类型

变量名有那些命名规范：
1。字母，数字，下划线，其他的特殊符号不行
2,不能数字开头
3，不能使用关键字
4，严格区分大小写
'''

name = '张三'
age = 19

a1 = 10
# 2 = 200


# 见名知义：getnamebyline
# getNameByLine  驼峰式：  开头第一个单词全部小写
#
getNameByLine = 'hello'
get_name_by_line = 'hello'

# 大驼峰：  python  面向对象： 类名  每个单词的首字母大写
#
GetNameByLine = 'hello'

# 名字 = 'zhangshan' #汉字也可以使用，但会黄色提示，可能会报错
# print(名字)

i = 0
while i < 5:
    i += 1
    print('*' * i)


for i in range(1, 6):
    print('*' * i)