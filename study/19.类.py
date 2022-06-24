# print(type(12))
# # <class 'int'>    # 整数类型
# print(type('12'))
# # <class 'str'>    # 字符类型
# print(type([1, 2]))
# # <class 'list'>   # 列表类型
# print(type((1, 2)))
# # <class 'tuple'>  # 元组类型
# print(type({1: 2}))
# <class 'dict'>   # 字典类型


class aa:
    a = '杭州'
    b = '萧山'

    @staticmethod
    def function():
        print('哈哈')

    def __init__(self, c, d):
        self.c = c
        self.d = d


cc = aa('地球', '中国')
#
# cc.function()
print(cc.c)


class BenzCar:
    brand = '奔驰'
    country = '德国'

    @staticmethod
    def pressHorn():
        print('嘟嘟~~~~~~')
        # self代表实例本身，color代表参数，enginesn也是参数

    def __init__(self, color, engineSN):  # 实例化属性，实例才可以用的属性，非公用的
        self.color = color  # 颜色
        self.engineSN = engineSN  # 发动机编号

    def changeColor(self, newColor):
        self.color = newColor


class Benz2016(BenzCar):
    price = 580000
    model = 'Benz2016'


class Benz2018(BenzCar):
    price = 880000
    model = 'Benz2018'

    def __init__(self, color, engineSN, weight):
        # 先调用父类的初始化方法
        BenzCar.__init__(self, color, engineSN)
        self.weight = weight  # 车的重量
        self.oilweight = 0  # 油的重量

    # 加油
    def fillOil(self, oilAdded):
        self.oilweight += oilAdded
        self.weight += oilAdded


car1 = Benz2016('red', '234234545622')
car2 = Benz2018('blue', '111135545988', 100)

print(car1.brand)
print(car1.country)
car1.changeColor('black')
print(car1.color)

print(car2.brand)
print(car2.country)
car2.pressHorn()
print(car2.weight)
