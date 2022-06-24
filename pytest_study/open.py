import yaml
#

def yamlload(path):
    f = open(path, 'r', encoding='utf-8')
    data = yaml.load(f, Loader=yaml.FullLoader)
    return data
#
#
#
#
# if __name__ == "__main__":
#     a = yamlload('./study.yaml')
#     print(a)


