# coding: utf-8
from selenium import webdriver
import unittest


class WorldOfTanks_RU(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://worldoftanks.ru"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_SearchUser(self):
        driver = self.driver
        #todo: define steps
        driver.get(self.base_url + "/")
        driver.find_element_by_xpath("//li[6]/span").click()
        driver.find_element_by_link_text(u"Игроки").click()
        driver.find_element_by_id("account_table_search").click()
        driver.find_element_by_id("account_table_search").clear()
        driver.find_element_by_id("account_table_search").send_keys("ptluser2")
        driver.find_element_by_id("account-table-search-button").click()
        driver.find_element_by_link_text("ptluser2").click()
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

