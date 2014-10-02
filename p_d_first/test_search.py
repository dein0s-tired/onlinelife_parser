# coding: utf-8
from selenium import webdriver
from unittest import TestCase, main


class WorldOfTanksRU(TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = 'http://worldoftanks.ru'
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_search_player(self):
        driver = self.driver
        #todo: define steps
        #/community/accounts/
        driver.get(self.base_url + '/')
        driver.find_element_by_xpath("//li[6]/span").click()
        driver.find_element_by_xpath("//a[@href='/community/accounts/']").click()
        driver.find_element_by_id('account_table_search').click()
        driver.find_element_by_id('account_table_search').send_keys('ptluser2')
        driver.find_element_by_id('account-table-search-button').click()
        driver.find_element_by_link_text('ptluser2').click()
        #/community/
        driver.get(self.base_url + '/')
        driver.find_element_by_xpath("//a[@href='/community/']").click()
        driver.find_element_by_id('accounts_table_search').click()
        driver.find_element_by_id('accounts_table_search').send_keys('ptluser2')
        driver.find_element_by_id('account-table-search-button').click()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    main()

