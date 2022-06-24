'''
int
float
string
boolean

'''

money = 28  # 声明了一个名称叫money的变量，赋值为28

print(type(money))  # print()属于一个内置函数，负责输入结果

money = 288
print(type(money))
# money  是一个变量，后面的值是允许发生变化。

money = 28.9
print(money)
print(type(money))
# 通过type(变量名)输入变量类型

money = '1万'  # <class 'str'>  代表的就是字符串
print(money)
print(type(money))

# 那些是属于字符串，只要在''里面的就是字符串
money = '1000'
print(type(money))
money = "1000"
print(type(money))
money = "'1000'"
print(type(money))

message = '石龙说:"今天吃的挺饱！"'
print(message)
message = "石龙说:'今天吃的挺饱！'"
print(message)

shi = '''
             静夜思
   【作者】李白 【朝代】唐译文对照
       床前明月光，疑是地上霜。
       举头望明月，低头思故乡。
'''
print(shi)

# 布尔类型：True  False
# 开发中判断，比如：是否登录成功。。。。
isLogin = True  # 真
print(isLogin)
isLogin = False  # 假
print(isLogin)

print(type(isLogin))  # <class 'bool'> 布尔类型

