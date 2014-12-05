import ast
import datetime
from lxml import etree
import re
import urllib

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
        else:  # todo is it needed here?
            pass


def get_serial_info(link):
    files = []
    names = []
    serial_data = ast.literal_eval(urllib.urlopen(link).read())
    if 'playlist' not in serial_data['playlist'][0].keys():  # one season
        season = serial_data['playlist']
        for episode in season:
            files.append(episode['file'])
            names.append(episode['comment'])
    else:
        seasons = serial_data['playlist']
        for season in seasons:
            episodes = season['playlist']
            for episode in episodes:
                files.append(episode['file'])
                names.append(episode['comment'])
    print names[len(names)-1], files[len(files)-1]


def xml_track_factory(episodes):
    _now = datetime.datetime.now()
    playlist_path = 'd:\\PROJECTS\\github\\neverless-to-test\\parsing\\data\\'  # todo configurable or from some object
    playlist_name = str(datetime.datetime.now().second) + '.xspf'
    xml_playlist = etree.Element('playlist')
    xml_title_playlist = etree.SubElement(xml_playlist, 'title')
    xml_title_playlist.text = 'Playlist created  at %s' % _now
    xml_tracklist_playlist = etree.SubElement(xml_playlist, 'trackList')
    for episode in episodes:
        xml_track_tracklist = etree.SubElement(xml_tracklist_playlist, 'track')
        xml_location_track = etree.SubElement(xml_track_tracklist, 'location')
        xml_location_track.text = str(episode[0])
        xml_title_track = etree.SubElement(xml_track_tracklist, 'title')
        xml_title_track.text = str(episode[1])
    output = open(playlist_path + playlist_name, 'w+').write(
        etree.tostring(xml_playlist, pretty_print=True, encoding='utf-8'))
    return output

