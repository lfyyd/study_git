"""
  键值对  dict
  "key":"value"
  key 是参数名
  value 是参数值
  key是唯一的,并且不可变
   json 格式
"""
# 1. 创建一个键值对
dt = {'name':'梁枫','avg':'18'}
print(dt)

# 2.访问键值对需要通过键去访问,就是名称去访问,然后访问到的是值
print(dt['name'])

# 3.修改字段中的元素
dt['name'] = ['梁若晨']
print(dt)

# 4.增加字段中的元素,直接增加
dt['sex']= ['男']
print(dt)

# 5.增加一个键值对
dt['dizhi'] = '上海'
print(dt)

# 6.删除键值对 可以用key索引去删除
del dt['dizhi']
print(dt)
# 也可以通过函数去删除
dt.pop('sex')   # 键值对是通过key是删除的,不像元祖列表字符串一样通过序号
print(dt)
# 删除最后一个键值对
dt.popitem()
print(dt)

# 字典也可以转换
dt1 = {'name':'小明','avg':'21'}
print(type(str(dt1)))


# 7.以此获取字典中的key和value的值
dt3 = {'name':'梁枫','avg':'18','sex':'男'}
for x,y in dt3.items():
    print(x,y)

# 8.字典也可以判断
if 'name' in dt3:
    print('存在')
else:
    print('不存在')

# 9. 多个元素进行更新，如何更新
dt4 = {'user':'admin','word':'123456'}
dt5 = {}
dt5.update(dt4)
print(dt5) #{'user': 'admin', 'word': '123456'}