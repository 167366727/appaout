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
    #登录测试
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

    #药物提醒设置测试
    def test__2(self):
        self.driver.find_element_by_xpath("//*[@text='测试']").click()
        self.driver.find_element_by_xpath("//*[@text='立即更新']").click()
        self.driver.find_element_by_xpath("//*[@text='我的随访']").click()
        self.driver.find_element_by_xpath(
            "//*[@text='提醒设置' and ./parent::*[(./preceding-sibling::* | ./following-sibling::*)[@text='随访计划']]]").click()
        self.driver.find_element_by_xpath("//*[@text='添加提醒']").click()
        self.driver.find_element_by_xpath("//*[@text='选择药物']").click()
        self.driver.find_element_by_xpath("//*[@text='雅施达']").click()
        self.driver.find_element_by_xpath("//*[@text='添加']").click()
        self.driver.find_element_by_xpath("//*[@text='00:00']").click()
        self.driver.swipe(270, 2267, 267, 2043, 2383)
        self.driver.swipe(832, 2127, 810, 1413, 912)
        self.driver.find_element_by_xpath("//*[@text='确认']").click()
        self.driver.find_element_by_xpath("//*[@text='完成']").click()
        self.driver.find_element_by_xpath("//*[@text='每天']").click()
        self.driver.find_element_by_xpath("//*[@text='每天' and @class='android.widget.Button']").click()
        self.driver.find_element_by_xpath("//*[@text='确认']").click()
        self.driver.find_element_by_xpath("//*[@text='单位']").click()
        self.driver.find_element_by_xpath("//*[@text='克(g)']").click()
        self.driver.find_element_by_xpath("//*[@text='确认']").click()
        self.driver.find_element_by_xpath(
            "//*[@class='android.widget.EditText' and (./preceding-sibling::* | ./following-sibling::*)[@text='剂量']]").send_keys(
            '5')
        self.driver.find_element_by_xpath("//*[@text='完成']").click()

    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()
