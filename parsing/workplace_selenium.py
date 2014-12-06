# coding=utf-8
import os
from selenium import webdriver
from waiting import wait as wait_lib

__author__ = 'dein0s'


class BrowserPhantomJS(object):
    def __init__(self):
        self.driver = webdriver.PhantomJS('phantomjs.exe')
        self.main_url = 'http://www.online-life.me/'
        self.fav_url = 'http://www.online-life.me/favorites/'
        self.user = os.getenv('LIFE_USER')
        self.password = os.getenv('LIFE_PWD')
        self.timeout = 60

    def wait(self, *args, **kwargs):
        """
        Wrapping 'wait()' method of 'waiting' library with default parameter values
        """
        predicate = args[0]
        expected_exceptions = kwargs.pop('expected_exceptions', [])

        def handled_exceptions_predicate():
            try:
                return predicate()
            except Exception as e:
                if not filter(lambda x: isinstance(e, x), expected_exceptions):
                    raise

        args = [handled_exceptions_predicate] + list(args[1:])
        params = {'timeout_seconds': self.timeout,
                  'sleep_seconds': (1, None)}
        params.update(kwargs)
        return wait_lib(*args, **params)

    def open_fav_url_and_login(self):
        login_link_xpath = '//div[contains(@class, "loginpanel")]/a[contains(@class, "btn-drop")]'
        login_name_xpath = '//input[contains(@name, "login_name")]'
        login_pwd_xpath = '//input[contains(@name, "login_password")]'
        login_submit_xpath = '//input[contains(@type, "submit")]'
        self.driver.get(self.main_url)
        login_link = self.driver.find_element_by_xpath(login_link_xpath)
        login_link.click()
        input_name = self.driver.find_element_by_xpath(login_name_xpath)
        input_name.send_keys(self.user)
        input_pwd = self.driver.find_element_by_xpath(login_pwd_xpath)
        input_pwd.send_keys(self.password)
        submit = self.driver.find_element_by_xpath(login_submit_xpath)
        submit.click()
        fav_link_xpath = '//div[contains(@class, "loginpanel")]/a[contains(@href, "%s")]' % self.fav_url
        favorite_link = self.driver.find_element_by_xpath(fav_link_xpath)
        self.wait(lambda: favorite_link.is_displayed())
        favorite_link.click()
        sort_order_panel = self.driver.find_element_by_id('news_set_sort')
        self.wait(lambda: sort_order_panel.is_displayed())

    def get_serials_links(self):  # todo visit all green links before close
        only_new_xpath = '//div[contains(@class, "custom-poster") and contains(@style, "background:lightgreen")]/a'
        serials_links = []
        self.open_fav_url_and_login()
        serial_posters = self.driver.find_elements_by_xpath(only_new_xpath)
        for item in serial_posters:
            item_link = item.get_attribute('href')
            serials_links.append(item_link)
        self.driver.get('http://www.online-life.me/index.php?action=logout')  # todo visit all links and close
        self.driver.close()
        return serials_links
