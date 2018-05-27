import pytest

class Test_01:
    @pytest.fixture()
    def fix(self):
        return [1,2]

    def test_001(self,fix):
        for i in fix:
            assert i == 2

if __name__ == '__main__':
    pytest.main("test_03lx02.py")
