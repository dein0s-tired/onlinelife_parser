# coding: utf-8
from selenium import webdriver
import unittest


class Selenium2ru(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url ='http://selenium2.ru'
        self.verificationErrors = []

    def test_clickDocuments(self):
        driver = self.driver
        driver.get(self.base_url + '/')
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/ul/li[2]/a').click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()