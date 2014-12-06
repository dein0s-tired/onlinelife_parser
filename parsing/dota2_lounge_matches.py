from unittest import TestCase
from selenium import webdriver

__author__ = 'dein0s'


class Dota2Lounge(TestCase):  # todo rework, deprecate TestCase class

    def test_matches(self):
        driver = webdriver.PhantomJS('f:\QA\installed\phantomJS\phantomjs.exe')
        driver.get('http://dota2lounge.com')
        matches = driver.find_elements_by_xpath('//*[@id="bets"]/div[contains(@class, "matchmain")]')
        start_time = driver.find_elements_by_xpath('//div[contains(@class, "matchheader")]/div[1]')
        for match in matches:
            curr = start_time.text.strip()
            print curr
