'''
  列表  list
'''

# 1.创建一个列表
lt = [1,2,3,4]
print(type(lt))

# 2.访问列表中的元素可以用切片的方式
a = [1, 2, 3.14, 'hello', [7,8,9] ]
print(a[0])   # 就是 1
print(a[1])   # 就是 2
print(a[4])    # 就是 [7,8,9]
print(a[-1])   # 也是 [7,8,9]
print(a[-4])   # 也是 2
print(a[-1][0])  # a[-1] 是[7,8,9],  a[-1][0] 就是 [7,8,9] 里面的第一个元素，就是 7
# 列表的切片也和字符串类似，想象用刀去切取其中的一部分，该在哪里下刀，就使用哪里的索引
a = [1, 2, 3.14, 'hello', [7,8,9] ]
print(a[0:3])    # 结果是   [1, 2, 3.14]
print(a[:3])        # 结果也是 [1, 2, 3.14]
print(a[3:5])     # 结果是   ['hello', [7,8,9] ]
print(a[3:])      # 结果也是 ['hello', [7,8,9] ]

print(a[-1][:2])  # 结果是   [7,8]   为什么？ 自己想一想

print(a)
# 结果还是 [1, 2, 3.14, 'hello', [7,8,9] ]
# 上面对a的切片操作是产生新的对象，并不会改变a指向的对象

# 3.修改列表内的元素
lt1 = [1,'hello',[7,8,9]]
print(type(lt1))
lt1[1] = '梁枫'
print(lt1)   # [1, '梁枫', [7, 8, 9]] 元素改变了

# 4.增加元素
lt1.append(666) # 在末尾加一个元素
print(lt1)

# 5.在指定的位置增加  insert
lt1.insert(0,0)  # 根据索引在索引前面增加
print(lt1)

# 6.增加多个元素   extend（）
lt2 = [2,3,4]
lt3 = [1]
lt3.extend(lt2)  # 拼接了多个列表
print(lt3)

# 7.删除元素
tp4 = [1,'hello',[7,8,9]]
# tp4.pop()  # 默认删除最后一个和append一样 [1, 'hello']
# print(tp4)
# 也可以指定删除
# tp4.pop(1)
# print(tp4)  # [1, [7, 8, 9]]

# del 函数删除方式
del tp4[-1]
print(tp4)  # [1, 'hello']


# 如果列表中有重复数据怎么办，只想删除其中一个怎么删除
lt5 = [6,6,7,8,9,123]
print(lt5.count(6))
print(lt5.index(6,0,len(lt5)))  # 查找
lt5.pop(0)
print(lt5)

# 8. 列表的升序降序排列
lt6 = [5,4,8,6,1,9]
lt6.sort()
print(lt6)
lt6.reverse()
print(lt6)
# 9.依次换取列表中的元素
for x in lt6:
    print(x,end='')
