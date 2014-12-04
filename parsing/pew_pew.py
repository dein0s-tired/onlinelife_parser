# coding=utf-8
__author__ = 'dein0s'

from selenium import webdriver
# import urllib2
import re

import os

import json
import pdb

# # pdb.set_trace()
# # driver = webdriver.PhantomJS('f:\QA\installed\phantomJS\phantomjs.exe')
# driver = webdriver.Firefox()
# # driver.set_page_load_timeout(100)
# # driver.set_window_size(1280, 1024)
# link_pattern = r'https?://[^\s<>"]+'
# driver.get('http://www.online-life.me/4819-oficery-2006-2009.html')
# player_object = driver.find_element_by_xpath('//div/center/object[contains(@id, "video")]/'
# 'param[contains(@name, "flashvars")]')
# value = player_object.get_attribute('value')
# playlist_link = re.compile(link_pattern).findall(value)
# driver.get(playlist_link)
# #
# playlist_data = driver.find_element_by_xpath('//body').text.strip()
#
# # text = {"playlist":[ {"comment":"ÐžÑ„Ð¸Ñ†ÐµÑ€Ñ‹ - 01 ÑÐµÐ·Ð¾Ð½", "playlist":[ {"comment":"ÐžÑ„Ð¸Ñ†ÐµÑ€Ñ‹ - 01 ÑÐµÐ·Ð¾Ð½, 01 ÑÐµÑ€Ð¸Ñ","file":"http://video30.online-life.me/video/f3a5bc29e7778cabb1c283342b718cee/qqeWmqylmZCdnLOnm5GqpZPX492n693br6I/tync/temp_video2/serials3/Oficeri_2006/s_01/Oficeri.s01e01.flv or http://video2.online-life.me/video/f3a5bc29e7778cabb1c283342b718cee/qqeWmqylmZCdnLOnm5GqpZPX492n693br6I/tync/temp_video2/serials3/Oficeri_2006/s_01/Oficeri.s01e01.flv","download":"http://video2.online-life.me/video/f3a5bc29e7778cabb1c283342b718cee/qqeWmqylmZCdnLOnm5GqpZPX492n693br6I/tync/temp_video2/serials3/Oficeri_2006/s_01/Oficeri.s01e01.mp4"}, {"comment":"ÐžÑ„Ð¸Ñ†ÐµÑ€Ñ‹ - 01 ÑÐµÐ·Ð¾Ð½, 02 ÑÐµÑ€Ð¸Ñ","file":"http://video30.online-life.me/video/f3a5bc29e7778cabb1c283342b718cee/qqeWmqylmZCdnLOnm5GqpZPX492n693br6I/tync/temp_video2/serials3/Oficeri_2006/s_01/Oficeri.s01e02.flv or http://video2.online-life.me/video/f3a5bc29e7778cabb1c283342b718cee/qqeWmqylmZCdnLOnm5GqpZPX492n693br6I/tync/temp_video2/serials3/Oficeri_2006/s_01/Oficeri.s01e02.flv","download":"http://video2.online-life.me/video/f3a5bc29e7778cabb1c283342b718cee/qqeWmqylmZCdnLOnm5GqpZPX492n693br6I/tync/temp_video2/serials3/Oficeri_2006/s_01/Oficeri.s01e02.mp4"}, {"comment":"ÐžÑ„Ð¸Ñ†ÐµÑ€Ñ‹ - 01 ÑÐµÐ·Ð¾Ð½, 03 ÑÐµÑ€Ð¸Ñ","file":"http://video30.online-life.me/video/f3a5bc29e7778cabb1c283342b718cee/qqeWmqylmZCdnLOnm5GqpZPX492n693br6I/tync/temp_video2/serials3/Oficeri_2006/s_01/Oficeri.s01e03.flv or http://video2.online-life.me/video/f3a5bc29e7778cabb1c283342b718cee/qqeWmqylmZCdnLOnm5GqpZPX492n693br6I/tync/temp_video2/serials3/Oficeri_2006/s_01/Oficeri.s01e03.flv","download":"http://video2.online-life.me/video/f3a5bc29e7778cabb1c283342b718cee/qqeWmqylmZCdnLOnm5GqpZPX492n693br6I/tync/temp_video2/serials3/Oficeri_2006/s_01/Oficeri.s01e03.mp4"}, {"comment":"ÐžÑ„Ð¸Ñ†ÐµÑ€Ñ‹ - 01 ÑÐµÐ·Ð¾Ð½, 04 ÑÐµÑ€Ð¸Ñ","file":"http://video30.online-life.me/video/f3a5bc29e7778cabb1c283342b718cee/qqeWmqylmZCdnLOnm5GqpZPX492n693br6I/tync/temp_video2/serials3/Oficeri_2006/s_01/Oficeri.s01e04.flv or http://video2.online-life.me/video/f3a5bc29e7778cabb1c283342b718cee/qqeWmqylmZCdnLOnm5GqpZPX492n693br6I/tync/temp_video2/serials3/Oficeri_2006/s_01/Oficeri.s01e04.flv","download":"http://video2.online-life.me/video/f3a5bc29e7778cabb1c283342b718cee/qqeWmqylmZCdnLOnm5GqpZPX492n693br6I/tync/temp_video2/serials3/Oficeri_2006/s_01/Oficeri.s01e04.mp4"}, {"comment":"ÐžÑ„Ð¸Ñ†ÐµÑ€Ñ‹ - 01 ÑÐµÐ·Ð¾Ð½, 05 ÑÐµÑ€Ð¸Ñ","file":"http://video30.online-life.me/video/f3a5bc29e7778cabb1c283342b718cee/qqeWmqylmZCdnLOnm5GqpZPX492n693br6I/tync/temp_video2/serials3/Oficeri_2006/s_01/Oficeri.s01e05.flv or http://video2.online-life.me/video/f3a5bc29e7778cabb1c283342b718cee/qqeWmqylmZCdnLOnm5GqpZPX492n693br6I/tync/temp_video2/serials3/Oficeri_2006/s_01/Oficeri.s01e05.flv","download":"http://video2.online-life.me/video/f3a5bc29e7778cabb1c283342b718cee/qqeWmqylmZCdnLOnm5GqpZPX492n693br6I/tync/temp_video2/serials3/Oficeri_2006/s_01/Oficeri.s01e05.mp4"}, {"comment":"ÐžÑ„Ð¸Ñ†ÐµÑ€Ñ‹ - 01 ÑÐµÐ·Ð¾Ð½, 06 ÑÐµÑ€Ð¸Ñ","file":"http://video30.online-life.me/video/f3a5bc29e7778cabb1c283342b718cee/qqeWmqylmZCdnLOnm5GqpZPX492n693br6I/tync/temp_video2/serials3/Oficeri_2006/s_01/Oficeri.s01e06.flv or http://video2.online-life.me/video/f3a5bc29e7778cabb1c283342b718cee/qqeWmqylmZCdnLOnm5GqpZPX492n693br6I/tync/temp_video2/serials3/Oficeri_2006/s_01/Oficeri.s01e06.flv","download":"http://video2.online-life.me/video/f3a5bc29e7778cabb1c283342b718cee/qqeWmqylmZCdnLOnm5GqpZPX492n693br6I/tync/temp_video2/serials3/Oficeri_2006/s_01/Oficeri.s01e06.mp4"}, {"comment":"ÐžÑ„Ð¸Ñ†ÐµÑ€Ñ‹ - 01 ÑÐµÐ·Ð¾Ð½, 07 ÑÐµÑ€Ð¸Ñ","file":"http://video30.online-life.me/video/f3a5bc29e7778cabb1c283342b718cee/qqeWmqylmZCdnLOnm5GqpZPX492n693br6I/tync/temp_video2/serials3/Oficeri_2006/s_01/Oficeri.s01e07.flv or http://video2.online-life.me/video/f3a5bc29e7778cabb1c283342b718cee/qqeWmqylmZCdnLOnm5GqpZPX492n693br6I/tync/temp_video2/serials3/Oficeri_2006/s_01/Oficeri.s01e07.flv","download":"http://video2.online-life.me/video/f3a5bc29e7778cabb1c283342b718cee/qqeWmqylmZCdnLOnm5GqpZPX492n693br6I/tync/temp_video2/serials3/Oficeri_2006/s_01/Oficeri.s01e07.mp4"}, {"comment":"ÐžÑ„Ð¸Ñ†ÐµÑ€Ñ‹ - 01 ÑÐµÐ·Ð¾Ð½, 08 ÑÐµÑ€Ð¸Ñ","file":"http://video30.online-life.me/video/f3a5bc29e7778cabb1c283342b718cee/qqeWmqylmZCdnLOnm5GqpZPX492n693br6I/tync/temp_video2/serials3/Oficeri_2006/s_01/Oficeri.s01e08.flv or http://video2.online-life.me/video/f3a5bc29e7778cabb1c283342b718cee/qqeWmqylmZCdnLOnm5GqpZPX492n693br6I/tync/temp_video2/serials3/Oficeri_2006/s_01/Oficeri.s01e08.flv","download":"http://video2.online-life.me/video/f3a5bc29e7778cabb1c283342b718cee/qqeWmqylmZCdnLOnm5GqpZPX492n693br6I/tync/temp_video2/serials3/Oficeri_2006/s_01/Oficeri.s01e08.mp4"} ] }, {"comment":"ÐžÑ„Ð¸Ñ†ÐµÑ€Ñ‹ - 02 ÑÐµÐ·Ð¾Ð½", "playlist":[ {"comment":"ÐžÑ„Ð¸Ñ†ÐµÑ€Ñ‹ - 02 ÑÐµÐ·Ð¾Ð½, 01 ÑÐµÑ€Ð¸Ñ","file":"http://video30.online-life.me/video/f3a5bc29e7778cabb1c283342b718cee/qqeWmqylmZCdnLOnm5GqpZPX492n693br6I/tync/temp_video2/serials3/Oficeri_2006/s_02/Oficeri.s02e01.flv or http://video2.online-life.me/video/f3a5bc29e7778cabb1c283342b718cee/qqeWmqylmZCdnLOnm5GqpZPX492n693br6I/tync/temp_video2/serials3/Oficeri_2006/s_02/Oficeri.s02e01.flv","download":"http://video2.online-life.me/video/f3a5bc29e7778cabb1c283342b718cee/qqeWmqylmZCdnLOnm5GqpZPX492n693br6I/tync/temp_video2/serials3/Oficeri_2006/s_02/Oficeri.s02e01.mp4"}, {"comment":"ÐžÑ„Ð¸Ñ†ÐµÑ€Ñ‹ - 02 ÑÐµÐ·Ð¾Ð½, 02 ÑÐµÑ€Ð¸Ñ","file":"http://video30.online-life.me/video/f3a5bc29e7778cabb1c283342b718cee/qqeWmqylmZCdnLOnm5GqpZPX492n693br6I/tync/temp_video2/serials3/Oficeri_2006/s_02/Oficeri.s02e02.flv or http://video2.online-life.me/video/f3a5bc29e7778cabb1c283342b718cee/qqeWmqylmZCdnLOnm5GqpZPX492n693br6I/tync/temp_video2/serials3/Oficeri_2006/s_02/Oficeri.s02e02.flv","download":"http://video2.online-life.me/video/f3a5bc29e7778cabb1c283342b718cee/qqeWmqylmZCdnLOnm5GqpZPX492n693br6I/tync/temp_video2/serials3/Oficeri_2006/s_02/Oficeri.s02e02.mp4"}, {"comment":"ÐžÑ„Ð¸Ñ†ÐµÑ€Ñ‹ - 02 ÑÐµÐ·Ð¾Ð½, 03 ÑÐµÑ€Ð¸Ñ","file":"http://video30.online-life.me/video/f3a5bc29e7778cabb1c283342b718cee/qqeWmqylmZCdnLOnm5GqpZPX492n693br6I/tync/temp_video2/serials3/Oficeri_2006/s_02/Oficeri.s02e03.flv or http://video2.online-life.me/video/f3a5bc29e7778cabb1c283342b718cee/qqeWmqylmZCdnLOnm5GqpZPX492n693br6I/tync/temp_video2/serials3/Oficeri_2006/s_02/Oficeri.s02e03.flv","download":"http://video2.online-life.me/video/f3a5bc29e7778cabb1c283342b718cee/qqeWmqylmZCdnLOnm5GqpZPX492n693br6I/tync/temp_video2/serials3/Oficeri_2006/s_02/Oficeri.s02e03.mp4"}, {"comment":"ÐžÑ„Ð¸Ñ†ÐµÑ€Ñ‹ - 02 ÑÐµÐ·Ð¾Ð½, 04 ÑÐµÑ€Ð¸Ñ","file":"http://video30.online-life.me/video/f3a5bc29e7778cabb1c283342b718cee/qqeWmqylmZCdnLOnm5GqpZPX492n693br6I/tync/temp_video2/serials3/Oficeri_2006/s_02/Oficeri.s02e04.flv or http://video2.online-life.me/video/f3a5bc29e7778cabb1c283342b718cee/qqeWmqylmZCdnLOnm5GqpZPX492n693br6I/tync/temp_video2/serials3/Oficeri_2006/s_02/Oficeri.s02e04.flv","download":"http://video2.online-life.me/video/f3a5bc29e7778cabb1c283342b718cee/qqeWmqylmZCdnLOnm5GqpZPX492n693br6I/tync/temp_video2/serials3/Oficeri_2006/s_02/Oficeri.s02e04.mp4"}, {"comment":"ÐžÑ„Ð¸Ñ†ÐµÑ€Ñ‹ - 02 ÑÐµÐ·Ð¾Ð½, 05 ÑÐµÑ€Ð¸Ñ","file":"http://video30.online-life.me/video/f3a5bc29e7778cabb1c283342b718cee/qqeWmqylmZCdnLOnm5GqpZPX492n693br6I/tync/temp_video2/serials3/Oficeri_2006/s_02/Oficeri.s02e05.flv or http://video2.online-life.me/video/f3a5bc29e7778cabb1c283342b718cee/qqeWmqylmZCdnLOnm5GqpZPX492n693br6I/tync/temp_video2/serials3/Oficeri_2006/s_02/Oficeri.s02e05.flv","download":"http://video2.online-life.me/video/f3a5bc29e7778cabb1c283342b718cee/qqeWmqylmZCdnLOnm5GqpZPX492n693br6I/tync/temp_video2/serials3/Oficeri_2006/s_02/Oficeri.s02e05.mp4"}, {"comment":"ÐžÑ„Ð¸Ñ†ÐµÑ€Ñ‹ - 02 ÑÐµÐ·Ð¾Ð½, 06 ÑÐµÑ€Ð¸Ñ","file":"http://video30.online-life.me/video/f3a5bc29e7778cabb1c283342b718cee/qqeWmqylmZCdnLOnm5GqpZPX492n693br6I/tync/temp_video2/serials3/Oficeri_2006/s_02/Oficeri.s02e06.flv or http://video2.online-life.me/video/f3a5bc29e7778cabb1c283342b718cee/qqeWmqylmZCdnLOnm5GqpZPX492n693br6I/tync/temp_video2/serials3/Oficeri_2006/s_02/Oficeri.s02e06.flv","download":"http://video2.online-life.me/video/f3a5bc29e7778cabb1c283342b718cee/qqeWmqylmZCdnLOnm5GqpZPX492n693br6I/tync/temp_video2/serials3/Oficeri_2006/s_02/Oficeri.s02e06.mp4"}, {"comment":"ÐžÑ„Ð¸Ñ†ÐµÑ€Ñ‹ - 02 ÑÐµÐ·Ð¾Ð½, 07 ÑÐµÑ€Ð¸Ñ","file":"http://video30.online-life.me/video/f3a5bc29e7778cabb1c283342b718cee/qqeWmqylmZCdnLOnm5GqpZPX492n693br6I/tync/temp_video2/serials3/Oficeri_2006/s_02/Oficeri.s02e07.flv or http://video2.online-life.me/video/f3a5bc29e7778cabb1c283342b718cee/qqeWmqylmZCdnLOnm5GqpZPX492n693br6I/tync/temp_video2/serials3/Oficeri_2006/s_02/Oficeri.s02e07.flv","download":"http://video2.online-life.me/video/f3a5bc29e7778cabb1c283342b718cee/qqeWmqylmZCdnLOnm5GqpZPX492n693br6I/tync/temp_video2/serials3/Oficeri_2006/s_02/Oficeri.s02e07.mp4"}, {"comment":"ÐžÑ„Ð¸Ñ†ÐµÑ€Ñ‹ - 02 ÑÐµÐ·Ð¾Ð½, 08 ÑÐµÑ€Ð¸Ñ","file":"http://video30.online-life.me/video/f3a5bc29e7778cabb1c283342b718cee/qqeWmqylmZCdnLOnm5GqpZPX492n693br6I/tync/temp_video2/serials3/Oficeri_2006/s_02/Oficeri.s02e08.flv or http://video2.online-life.me/video/f3a5bc29e7778cabb1c283342b718cee/qqeWmqylmZCdnLOnm5GqpZPX492n693br6I/tync/temp_video2/serials3/Oficeri_2006/s_02/Oficeri.s02e08.flv","download":"http://video2.online-life.me/video/f3a5bc29e7778cabb1c283342b718cee/qqeWmqylmZCdnLOnm5GqpZPX492n693br6I/tync/temp_video2/serials3/Oficeri_2006/s_02/Oficeri.s02e08.mp4"} ] } ]}
#
# # o = json.dumps(text)
# # print text
# text = json.loads(playlist_data)
# episode_links = re.compile(link_pattern).findall(text['playlist'][1]['playlist'][7]['file'])
# print episode_links
# # driver.close()


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
