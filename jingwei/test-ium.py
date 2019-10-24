import unittest
import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class __(unittest.TestCase):
    reportDirectory = 'reports'
    reportFormat = 'xml'
    dc = {}
    testName = '登录'
    driver = None

    def setUp(self):
        self.dc['reportDirectory'] = self.reportDirectory
        self.dc['reportFormat'] = self.reportFormat
        self.dc['testName'] = self.testName
        self.dc['udid'] = 'DWVNW19801011181'
        self.dc['appPackage'] = 'com.huidr.HuiDrPatient.debug'
        self.dc['appActivity'] = 'com.huidr.HuiDrPatient.activity.SplashActivity'
        self.dc['platformName'] = 'android'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.dc)

    def test__(self):
        self.driver.find_element_by_xpath("//*[@text='测试']").click()
        self.driver.find_element_by_xpath("//*[@text='立即更新']").click()
        self.driver.find_element_by_xpath(
            "//*[@class='android.widget.EditText' and (./preceding-sibling::* | ./following-sibling::*)[@text='+86']]").send_keys(
            '19822799040')
        self.driver.find_element_by_xpath(
            "//*[@class='android.widget.EditText' and (./preceding-sibling::* | ./following-sibling::*)[@text='获取验证码']]").send_keys(
            '1234')
        self.driver.find_element_by_xpath("//*[@text='获取验证码']").click()
        self.driver.find_element_by_xpath("//*[@text='登录']").click()

    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()
