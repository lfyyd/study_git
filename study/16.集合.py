"""
   集合 set
"""
# 1. 创建一个集合
set = {1, 2, 3, 4, 5, 2, 3, 4, 'liangfeng'}
print(set, type(set))

# 2.创建一个空的集合
set1 = {}
print(set1, type(set))

# 3.访问集合  因为集合是无序的,所以没法访问
# print(set[0])

# 4.集合支持那些运算符
# a&b   交集:公共的地方
# a|b   并集:全部元素去重
# a-b   差集:就是减法

# 5.集合元素操作的相关函数
# 1.增加元素
set.add(20)
print(set)
# 2.删除元素
set.pop()  # pop在集合里面是随机删除的
print(set)
# 3.remore删除
set.remove(20)
print(set)

# 6.常用的判断函数
# 1.判断返回有没有重复的元素集合
set2 = {1,2,3,4,5,6}
set3 = {1,2,3,'shanghai'}
print(set2.issubset(set3))
print(set2.issuperset(set3))

