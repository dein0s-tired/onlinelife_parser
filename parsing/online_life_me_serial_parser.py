# coding=utf-8
import ast
import datetime
import re
import urllib
from lxml import etree
from tests_more import Profiler, get_link as get_playlist_links, timer
from workplace_selenium import BrowserPhantomJS

__author__ = 'dein0s'


# def get_link():
#     url = 'http://www.online-life.me/783-mentalist-onlayn.html'
#     url_pattern = r'https?://[^\s<>"]+'
#     playlist_pattern = 'all_s.txt'
#     txt = urllib.urlopen(url).read()
#     links = re.compile(url_pattern).findall(txt)
#     for single_link in links:
#         if single_link.find(playlist_pattern) > -1:
#             return single_link


def get_single_serial_data(serial_playlist_url, get_first=True, only_last_episode=True):
    all_serial_episodes = []
    last_serial_episode = []
    if type(serial_playlist_url) is str:
        serial_data = ast.literal_eval(urllib.urlopen(serial_playlist_url).read())
        if 'playlist' not in serial_data['playlist'][0].keys():  # one season
            season = serial_data['playlist']
            for episode in season:
                has_two_links = episode['file'].find(' or ')
                episode_title = episode['comment']
                episode_file = episode['file']
                first_link = episode_file.split(' or ')[0]
                second_link = episode_file.split(' or ')[1]
                if has_two_links != -1:
                    all_serial_episodes.append([episode_title, first_link if get_first else second_link])
                else:
                    all_serial_episodes.append([episode_title, episode_file])
        else:
            seasons = serial_data['playlist']
            for season in seasons:
                episodes = season['playlist']
                for episode in episodes:
                    has_two_links = episode['file'].find(' or ')
                    episode_title = episode['comment']
                    episode_file = episode['file']
                    first_link = episode_file.split(' or ')[0]
                    second_link = episode_file.split(' or ')[1]
                    if has_two_links != -1:
                        all_serial_episodes.append([episode_title, first_link if get_first else second_link])
                    else:
                        all_serial_episodes.append([episode_title, episode_file])
        if only_last_episode:
            last_serial_episode.append(all_serial_episodes[-1])
            return last_serial_episode
        else:
            return all_serial_episodes
    elif type(serial_playlist_url) is list:
        raise TypeError(
            'serial_playlist_url must be <str>, got %s. Consider using "get_multiple_serials_data" method.' % type(
                serial_playlist_url))
    else:
        raise TypeError('serial_playlist_url must be <str>, got %s' % type(serial_playlist_url))


def get_multiple_serials_data(serials_playlist_urls, only_last_episode=True):
    all_serials_episodes = []
    if type(serials_playlist_urls) is list:
        for url in serials_playlist_urls:
            serial_episodes = get_single_serial_data(url, only_last_episode)
            all_serials_episodes += serial_episodes
    elif type(serials_playlist_urls) is str:
        raise TypeError(
            'serials_playlist_urls must be <list>, got %s. Consider using "get_single_serial_data" method.' % type(
                serials_playlist_urls))
    else:
        raise TypeError('serials_playlist_urls must be <list>, got %s' % type(serials_playlist_urls))
    return all_serials_episodes


def xml_track_factory(episodes):
    _now = datetime.datetime.now()
    playlist_name = str(datetime.datetime.now().second) + '.xspf'
    counter = 0
    # dirty hacks to add extended namespace
    playlist_namespace = 'http://xspf.org/ns/0/'
    playlist = '{%s}' % playlist_namespace
    nsmap = {None: playlist_namespace}
    temp_playllist = etree.Element(playlist + 'playlist', nsmap=nsmap)
    vlc = 'http://www.videolan.org/vlc/playlist/ns/0/'
    nsmap['vlc'] = vlc
    root = etree.ElementTree(element=temp_playllist).getroot()
    xml_playlist = etree.Element(root.tag, nsmap=nsmap)
    xml_playlist[:] = root[:]
    xml_playlist.set('version', '1')
    # dirty hacks to add extended namespace
    xml_title_playlist = etree.SubElement(xml_playlist, 'title')
    xml_title_playlist.text = 'Playlist created  at %s' % _now
    xml_tracklist_playlist = etree.SubElement(xml_playlist, 'trackList')
    xml_extension_playlist = etree.SubElement(xml_playlist, 'extension')
    xml_extension_playlist.set('application', 'http://www.videolan.org/vlc/playlist/0')
    for episode in episodes:
        xml_track_tracklist = etree.SubElement(xml_tracklist_playlist, 'track')
        xml_location_track = etree.SubElement(xml_track_tracklist, 'location')
        xml_location_track.text = episode[1].decode('utf-8')
        xml_title_track = etree.SubElement(xml_track_tracklist, 'title')
        xml_title_track.text = episode[0].decode('utf8')
        xml_extension_track = etree.SubElement(xml_track_tracklist, 'extension')
        xml_extension_track.set('application', 'http://www.videolan.org/vlc/playlist/0')
        xml_id_extension = etree.Element('{%s}%s' % (vlc, 'id'))
        xml_id_extension.text = str(counter).decode('utf-8')
        xml_option_extension = etree.Element('{%s}%s' % (vlc, 'option'))
        xml_option_extension.text = 'network-caching=3000'
        xml_extension_track.append(xml_id_extension)
        xml_extension_track.append(xml_option_extension)
        xml_item_extension = etree.Element('{%s}%s' % (vlc, 'item'), tid=str(counter).decode('utf-8'))
        xml_extension_playlist.append(xml_item_extension)
        counter += 1
    output = open(playlist_name, 'w+').write(
        etree.tostring(xml_playlist, xml_declaration=True, pretty_print=True, encoding='utf-8'))
    return output


@timer
def test_run():
    # url1 = 'http://www.online-life.me/1136-elementarno-2012.html'
    # url2 = 'http://www.online-life.me/1253-morskaya-policiya-los-andzheles.html'
    # url3 = 'http://www.online-life.me/783-mentalist-onlayn.html'
    # url4 = 'http://www.online-life.me/1173-strela-2012.html'
    # url5 = 'http://www.online-life.me/296-kasl-online-all-seasons.html'
    # url6 = 'http://www.online-life.me/4423-morskaya-policiya-novyy-orlean-2014.html'
    # with Profiler:
    # urls = BrowserPhantomJS().get_serials_links()
    # urls = ['http://www.online-life.me/4825-operaciya-cvet-nacii-2004.html', '']
    # link = get_playlist_links(urls)
    # url = 'http://www.online-life.me/4279-skorpion-2014.html'
    # urls = [url]
    # link = get_playlist_links(urls)  # todo smth is wrong here
    link = 'http://www.online-life.me/pls3/0a254cb678c8c45ecfe232653f4c9d3b/qqeWnK2nlo-kmrOklZyjpJiRmd3x65Pb7eqfjw/pl_skorpion.2014_all_s.txt'
    # todo execute from cmd with args
    data = get_single_serial_data(serial_playlist_url=link, get_first=True, only_last_episode=False)
    return xml_track_factory(data)

test_run()