'''
文件操作的步骤
打开open (文件路劲，访问方式)
读取数据: read     f = open('test.txt','w')
写入数据: write    f = write('liangfeng')
关闭文件: close()  f.close()
注意一定要关闭文件，要不然占用资源
'''

# f = open('file.yaml', 'r', encoding='utf-8')
# # f.write('梁枫:加油')
# content = f.read()
# print(type(content))
# f.close()
# name = content.split(':')[0]
# print(name)
import yaml

'''
读取文件操作，
read()      读取所有文件
readline()  读取一行文件
readlines() 一次性读取所有内容
'''

# 因为是读取文本文件的模式， 可以无须指定 mode参数
# 因为都是 英文字符，基本上所以的编码方式都兼容ASCII，可以无须指定encoding参数
# f = open('file.yaml')
# tmp = f.read(3)  # read 方法读取3个字符
# print(tmp)       # 返回3个字符的字符串 'hel'
# tmp = f.read(3)  # 继续使用 read 方法读取3个字符
# print(tmp)       # 返回3个字符的字符串 'lo\n'  换行符也是一个字符
# tmp = f.read()  # 不加参数，读取剩余的所有字符
# print(tmp)       # 返回剩余字符的字符串 'cHl0aG9uMy52aXAgYWxsIHJpZ2h0cyByZXNlcnZlZA=='
# # 文件操作完毕后， 使用close 方法关闭该文件对象
# f.close()




files = open('./file.yaml','r',encoding='utf-8')
# data = yaml.load(files,Loader=yaml.FullLoader)
# print(data['username'])
a = files.read()
b = a.split()
print(b[-1])
print(b[-3])
