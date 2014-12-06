# coding=utf-8
__author__ = 'dein0s'

from selenium import webdriver
# import urllib2
import re

import os

import json


class GetSerial(object):

    def __init__(self, serial_url=None):
        self.serial_url = serial_url if serial_url else None
        self.serial_name = None
        self.serial_translation = None
        self.serial_season = None
        self.serial_episode = None
        self.driver = webdriver.PhantomJS('f:\QA\installed\phantomJS_with_flash\phantomjs.exe')
        self.site_url = 'http://www.online-life.me/kino-serial/'  # todo reconfigure for personal list http://www.online-life.me/favorites/
        self.user = os.getenv('LIFE_USER')
        self.password = os.getenv('LIFE_PWD')

# todo add login method

    def get_links_for_episode_in_season(self):
        self.serial_season = 6
        self.serial_episode = 7
        # todo add login, grep all green elements
        # driver = webdriver.PhantomJS(
        #     'f:\QA\installed\phantomJS_with_flash\phantomjs.exe')  # phantomjs with flash support
        link_pattern = r'https?://[^\s<>"]+'
        self.driver.get(self.serial_url)
        player_object = self.driver.find_element_by_xpath('//param[contains(@name, "flashvars")]')
        playlist_link = re.compile(link_pattern).findall(player_object.get_attribute('value'))
        last_update_text = self.driver.find_element_by_xpath('//font[contains(@style, "font-weight:bold;font-size:18px")]').text.strip()  # todo filter multiple series
        self.driver.get(playlist_link)
        playlist_data = json.loads(self.driver.find_element_by_xpath('//body').text.strip())
        episode_links = re.compile(link_pattern).findall(playlist_data['playlist'][self.serial_season - 1]['playlist'][self.serial_episode - 1]['file'])
        self.driver.close()
        parts = str(episode_links[0]).strip('"/"')
        print parts
        # print '%s : %s' % (last_update_text, episode_links[0])

    def open_site(self):
        self.driver.get(self.serial_url)

    def get_serial_info_from_page(self):
        # driver = webdriver.PhantomJS('f:\QA\installed\phantomJS_with_flash\phantomjs.exe')  # phantomjs with flash support
        self.driver.get(self.site_url)
        # serials = self.driver.find_elements_by_xpath('//div[contains(@class, "custom-poster")]/a')
        # self.serial_name = []
        # for serial in serials:
        #     serial_info_raw = serial.text.strip()
        #     self.serial_name = (u''.join(re.findall(u'([а-яА-я]\s?)', serial_info_raw)).strip())
        #     self.serial_translation = re.findall('([a-zA-Z]{2,})', serial_info_raw)
        #     return self.serial_name, self.serial_translation
        serial = self.driver.find_element_by_xpath(
            '//div[contains(@class, "custom-poster")]/a[contains(@href, "%s")]' % self.serial_url)  # todo reconfigure for highlights in personal list
        serial_info_raw = serial.text.strip()
        self.serial_name = u''.join(re.findall(u'([а-яА-я]\s?)', serial_info_raw)).strip()
        self.serial_translation = re.findall('([a-zA-Z]{2,}\s?)', serial_info_raw)
        self.serial_season = []
        self.serial_episode = []
        for element in serial_info_raw.split(','):
            element_int_list = [int(s) for s in re.findall('\d+', element)]
            # self.serial_season.add(element_int_list[0])
            if element_int_list[0] not in self.serial_season:
                self.serial_season.append(element_int_list[0])
            if element_int_list[1] not in self.serial_episode:
                self.serial_episode.append(element_int_list[1])
        return self


url = 'http://www.online-life.me/1050-byvaet-i-huzhe-vse-sezony.html'
serial = GetSerial(serial_url=url).get_links_for_episode_in_season()
