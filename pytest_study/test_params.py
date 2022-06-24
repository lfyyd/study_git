'''
参数化用法
'''

import pytest


def test_a():
    print('这是1用例')


@pytest.mark.parametrize(
    'i',
    range(5)
)
def test_b(i):
    print(f'这是{i}用例')
