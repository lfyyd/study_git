'''

yaml是一种数据格式，它可以和json数据相互转化，一般自动化的项目当中用于做配置文件或者是测试用例文件
对于特殊数据类型，常态化的文件需要先读取内容，在基于数据转换，最终是现在所需要的数据类型。
yaml可以原汤化原食，对于特色数据类型的知此事非常优秀的
    list格式通过“- ”表示
    dict格式通过": "表示
    list和dict可以相互嵌套进行引用
yaml中的锚点与引用
    本事上而言，就是将数据冗余进行降低，把重复的数据复制成一个变量，在后续的数据内容中通过引用的方式，把变量引用进去
    &表示定义一个变量名称，在yaml中叫做锚点
    *表示引用定义好的变量，在yaml中叫做引用
    <<: 表示追加，就是在原本文件内容中进行追加
'''
import yaml


def read_yaml(path):
    try:
        f = open(path, 'r', encoding='utf-8')
        data = yaml.load(stream=f, Loader=yaml.FullLoader)
        print(data)
    except:
        print('没有要找的内容')


if __name__ == "__main__":
    read_yaml('./24.dict.yaml')
