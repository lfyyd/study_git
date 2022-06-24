import yaml


def loadyaml(path):
    file = open(path, 'r', encoding='utf-8')
    data = yaml.load(file, Loader=yaml.FullLoader)
    return data

# a = loadyaml('./user.yaml')
# print(a[0]['username'])