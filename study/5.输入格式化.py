name = '蔡徐坤'
age = 26

# 我喜欢听26岁的蔡徐坤唱歌
print('我喜欢听' + str(age) + '岁的' + name + '唱歌')
# 字符串如何进行格式化？
'''
符号：
%s 字符串  string
%d 整数   digit
%f 浮点数  float
'''
print('我喜欢听%d岁的%s唱歌' % (age, name))

money = 999.95
#26岁的蔡徐坤一首歌挣了999.95块钱
print('%d岁的%s一首歌挣了%f块钱'%(age,name,money))
print('%s岁的%s一首歌挣了%s块钱'%(age,name,money))
print('%d岁的%s一首歌挣了%.2f块钱'%(age,name,money))