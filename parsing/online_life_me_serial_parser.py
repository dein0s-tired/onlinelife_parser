# coding=utf-8
import ast
import datetime
import re
import urllib
from lxml import etree
from tests_more import Profiler

__author__ = 'dein0s'


def get_link():
    url = 'http://www.online-life.me/2377-bruklin-9-9-2013.html'
    url_pattern = r'https?://[^\s<>"]+'
    playlist_pattern = 'all_s.txt'
    txt = urllib.urlopen(url).read()
    links = re.compile(url_pattern).findall(txt)
    for single_link in links:
        if single_link.find(playlist_pattern) > -1:
            return single_link


def get_single_serial_data(serial_playlist_url, only_last_episode=True):
    all_serial_episodes = []
    last_serial_episode = []
    if type(serial_playlist_url) is str:
        serial_data = ast.literal_eval(urllib.urlopen(serial_playlist_url).read())
        if 'playlist' not in serial_data['playlist'][0].keys():  # one season
            season = serial_data['playlist']
            for episode in season:
                all_serial_episodes.append([episode['comment'], episode['file']])
        else:
            seasons = serial_data['playlist']
            for season in seasons:
                episodes = season['playlist']
                for episode in episodes:
                    all_serial_episodes.append([episode['comment'], episode['file']])
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
        xml_option_extension.text = 'network-caching=2000'
        xml_extension_track.append(xml_id_extension)
        xml_extension_track.append(xml_option_extension)
        xml_item_extension = etree.Element('{%s}%s' % (vlc, 'item'), tid=str(counter).decode('utf-8'))
        xml_extension_playlist.append(xml_item_extension)
        counter += 1
    output = open(playlist_name, 'w+').write(
        etree.tostring(xml_playlist, xml_declaration=True, pretty_print=True, encoding='utf-8'))
    return output


def test_run():
    with Profiler():
        link = get_link()
    with Profiler():
        data = get_single_serial_data(link, False)
    with Profiler():
        return xml_track_factory(data)

test_run()