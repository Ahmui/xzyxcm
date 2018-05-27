import pytest
from time import sleep
from appium import webdriver

class Test_01:

    def setup_class(self):
        desired_caps = {
            "platformName": "Android",
            "platformVersion": "5.1",
            "deviceName": "huawei",
            # "appActivity": "io.toutiao.android.ui.activity.MainActivity",
            # "appPackage": "io.manong.developerdaily"
            "appActivity": ".ui.ConversationList",
            "appPackage": "com.android.mms",
            "unicodeKeyboard": "True",
            "resetKeyboard": "True"

        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def teardown_class(self):
        sleep(3)
        self.driver.quit()

    # 定义一个函数，新建短信，添加手机号
    @pytest.fixture(scope="class",autouse=True)
    def add_meg(self):
        sleep(1)
        self.driver.find_element_by_id("com.android.mms:id/action_compose_new").click()
        sleep(1)
        self.driver.find_element_by_id("com.android.mms:id/recipients_editor").send_keys("1880-303-3683")

    @pytest.mark.parametrize("value",["123","hello","你好"])
    def test_001(self,value):
        self.driver.find_element_by_id("com.android.mms:id/embedded_text_editor").send_keys(value)
        self.driver.find_element_by_id("com.android.mms:id/send_button_sms").click()
        sleep(2)
        get_msg = self.driver.find_elements_by_id("com.android.mms:id/text_view")
        assert value in [i.text for i in get_msg]





if __name__ == "__main__":
    pytest.main("test_05dalx03.py")