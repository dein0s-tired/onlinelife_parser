# coding=utf-8
__author__ = 'dein0s'

from selenium import webdriver
# import urllib2
import re
import os
import json

from waiting import wait as wait_lib


class Browser(object):

    def __init__(self):
        self.driver = webdriver.PhantomJS('f:\QA\installed\phantomJS_with_flash\phantomjs.exe')
        # self.driver = webdriver.Firefox()
        self.main_url = 'http://www.online-life.me/'
        self.fav_url = 'http://www.online-life.me/favorites/'
        self.user = os.getenv('LIFE_USER')
        self.password = os.getenv('LIFE_PWD')
        self.timeout = 60
        # self.driver.implicitly_wait(self.timeout/3)

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
        login_name_xpath ='//input[contains(@name, "login_name")]'
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
        serial_block_xpath = '//div[contains(@class, "custom-poster")]/a'
        # only_new_xpath = '//div[contains(@class, "custom-poster") and contains(@style, "background:lightgreen")]/a'
        serials_links = []
        self.open_fav_url_and_login()
        serial_posters = self.driver.find_elements_by_xpath(serial_block_xpath)
        for item in serial_posters:
            item_link = item.get_attribute('href')
            serials_links.append(item_link)
        return serials_links

    def get_links_for_episode_in_season(self):
        serial_links = self.get_serials_links()
        self.driver.get('http://www.online-life.me/index.php?action=logout')
        # self.driver.close()
        playlist_links = []
        for link in serial_links:
            url_link_pattern = r'https?://[^\s<>"]+'
            self.driver.get(link)
            player_object = self.driver.find_element_by_xpath('//param[contains(@name, "flashvars")]')
            txt_link = re.compile(url_link_pattern).findall(player_object.get_attribute('value'))
            playlist_links.append(txt_link)
            # self.driver.get(txt_link)
            # playlist_data = json.loads(self.driver.find_element_by_xpath('//body')).text.strip()
            # print playlist_data
        self.driver.close()
        return playlist_links


        # # todo add login, grep all green elements
        # # driver = webdriver.PhantomJS(
        # #     'f:\QA\installed\phantomJS_with_flash\phantomjs.exe')  # phantomjs with flash support
        # link_pattern = r'https?://[^\s<>"]+'
        # # driver.get(url)
        # # player_object = driver.find_element_by_xpath('//param[contains(@name, "flashvars")]')
        # for item in player_object:
        #     playlist_link = re.compile(link_pattern).findall(player_object.get_attribute('value'))
        #     # last_update_text = driver.find_element_by_xpath('//font[contains(@style, "font-weight:bold;font-size:18px")]').text.strip()  # todo filter multiple series
        #     driver.get(playlist_link)
        #     playlist_data = json.loads(driver.find_element_by_xpath('//body').text.strip())
        #     # pdb.set_trace()
        #     #episode_links = re.compile(link_pattern).findall(playlist_data[u'playlist'][episode - 1]['file'])
        #     # episode_links = re.compile(link_pattern).findall(playlist_data[u'playlist'][season - 1]['playlist'][episode - 1]['file'])
        #     # parts = str(episode_links[0]).strip('"/"')
        # driver.close()
        # print playlist_data
        # # print episode_links


print Browser().get_links_for_episode_in_season()

"""
def get_player_object(driver, url):
    driver.get(url)
    player_object = driver.find_element_by_xpath('//param[contains(@name, "flashvars")]')
    # driver.close()
    return player_object


def get_links_for_episode_in_season(driver, player_object, season, episode):
    # todo add login, grep all green elements
    # driver = webdriver.PhantomJS(
    #     'f:\QA\installed\phantomJS_with_flash\phantomjs.exe')  # phantomjs with flash support
    link_pattern = r'https?://[^\s<>"]+'
    # driver.get(url)
    # player_object = driver.find_element_by_xpath('//param[contains(@name, "flashvars")]')
    for item in player_object:
        playlist_link = re.compile(link_pattern).findall(player_object.get_attribute('value'))
        # last_update_text = driver.find_element_by_xpath('//font[contains(@style, "font-weight:bold;font-size:18px")]').text.strip()  # todo filter multiple series
        driver.get(playlist_link)
        playlist_data = json.loads(driver.find_element_by_xpath('//body').text.strip())
        # pdb.set_trace()
        #episode_links = re.compile(link_pattern).findall(playlist_data[u'playlist'][episode - 1]['file'])
        # episode_links = re.compile(link_pattern).findall(playlist_data[u'playlist'][season - 1]['playlist'][episode - 1]['file'])
        # parts = str(episode_links[0]).strip('"/"')
    driver.close()
    print playlist_data
    # print episode_links

season = 1
episode = 8
url = 'http://www.online-life.me/4423-morskaya-policiya-novyy-orlean-2014.html'
driver = Browser().driver
pdata = get_player_object(driver, url)

print get_links_for_episode_in_season(driver, pdata, season, episode)

print get_links_for_episode_in_season(driver, url, season, episode)
"""