from time import sleep

import pytest


class Testone:

    @pytest.mark.run(order=4)
    # @pytest.mark.smoke
    def test_01(self):
        print('测试凉风')

    @pytest.mark.run(order=3)
    def test_02(self):
        print('测试梁枫')

    @pytest.mark.run(order=2)
    def test_03(self):
        print('测试若晨')

    @pytest.mark.run(order=1)
    # @pytest.mark.xfail
    def test_04(self):
        print('测试凉皮')

    # with pytest.raises(AssertionError):
    #     assert 1 == 2
