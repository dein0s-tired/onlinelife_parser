# coding=utf-8
import ast
from lxml import etree
import datetime
import re
import urllib
from timeit import timeit

import time


class Profiler(object):
    def __enter__(self):
        self._startTime = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print 'Elapsed time: {:.3f} sec'.format(time.time() - self._startTime)


def timer(f):
    def tmp(*args, **kwargs):
        t = time.time()
        res = f(*args, **kwargs)
        print "Total elapsed time: %f sec" % (time.time() - t)
        return res
    return tmp


def get_link(url):
    serials_playlists = []
    url_pattern = r'https?://[^\s<>"]+'  # simple url pattern
    # playlist_url_pattern = r'https?://[^\s<>"]+txt'
    # playlist_pattern = '.txt'
    for item in url:
        txt = urllib.urlopen(item).read()
        asasa = re.compile(url_pattern).findall(txt)
        playlist_link = re.compile(url_pattern).findall(txt)[0]
        serials_playlists.append(playlist_link)
    #     for single_link in links:
    #         if single_link.find(playlist_pattern) > -1:
    #             serials_playlists.append(single_link)
    #             break
    return serials_playlists

# urls = ['http://www.online-life.me/783-mentalist-onlayn.html', 'http://www.online-life.me/396-belyy-vorotnichok-smotret-onlayn-vse-sezony.html']
# print get_link(urls)
# # print get_link()
