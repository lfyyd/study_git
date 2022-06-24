'''
 在调用其他外面程序的时候可以用os库的system 函数
 使用os库的system函数，调用其他程序是非常方便的
 就把命令行内容作为system函数的参数即可
'''

import os
cmd = 'pip install selenium'  # 放自己的文件根目录和文件就可以了
# cmd = r'D:\JBen\JBen.Python http://baidu.com/nginx/ngix-1.13.9.zip'
os.system(cmd)

print('下载完毕')




