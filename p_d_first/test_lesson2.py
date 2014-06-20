__author__ = 'dein0s'

# coding: utf-8

from selenium import webdriver
import unittest


class Selenium2ru(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.baseURL ='http://selenium2.ru'
        self.verificationErrors = []
        self.accept_next_allert = True

    def test_clickDocuments(self):
        driver = self.driver
        driver.get(self.baseURL + '/')
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/ul/li[2]/a').click()

    def end_of_test(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()