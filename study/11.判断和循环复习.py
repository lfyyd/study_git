'''
流程控制：
条件语句:
   if  条件:
       pass
   if  条件:
       pass
   else:
       pass

   if  条件:
       pass
   elif  条件:
       pass
   elif  条件:
       pass
   else:
       pass

嵌套语句:
  if 条件:
     if 条件:
        pass
     elif 条件:
        pass
     else:
        pass
  elif 条件:
      pass
  else:
      pass

循环语句:
while: 1.初始值   2.条件  3.变量改变
    while True:  # 不确定循环几次时进行使用
       pass

    while True:
       pass
       break # 结束循环

    while True:
       pass
       continue  # 停止它下面所有打印
     whiler...else:


for:    # 有固定循环次数时进行使用
    for i in range(n):
        pass

    range(n):  0~n #不包括n
    range(1,n): 1~n #从1开始 到N前面   不包括n
    range(1,n,2): 1~n # 从1开始每隔2个数字 到N前面  最后一个是步长：2

    for .... else:


嵌套：
*
**
***
****
*****

 n = 1
 while n <= 5:  # 外层控制行数
     m = 0
     while m < n:  # 内存控制打印的是*
         print('*',end="")   end 控制打印后光标在本行
         m += 1
     n += 1
     print()    跳空格一行

'''
