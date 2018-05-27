import pytest,allure

class Test_001:
    @allure.step(title="测试步骤001")
    @pytest.mark.parametrize("a",[1,2,3])
    def test_adc(self,a):
        assert a!=2