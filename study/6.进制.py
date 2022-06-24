'''
二进制：0，1
八进制：0，1，2，3，4，5，6，7
十进制：0~10
十六进制:0~9  a~f

十进制转二进制：
10 ---》二进制表示：
'''

n = 149
result = bin(n)
print(result)

# 转八进制
result = oct(n)
print(result)

# 转十六进制
n = 221
result = hex(n)
print(result)

# 前缀： 0b 二进制  0o八进制  0x十六进制 默认十进制

'''
思考：
1，n = 0x558  怎么十进制输入？
2，已知 n =0x558,转成二进制？转成八进制？
'''
n = 0x558
parse = int(n)
print(parse)
