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

#
# @timer
# def get_link():
#     url = 'http://www.online-life.me/2377-bruklin-9-9-2013.html'
#     url_pattern = r'https?://[^\s<>"]+'
#     playlist_pattern = 'all_s.txt'
#     with Profiler():
#         txt = urllib.urlopen(url).read()
#     with Profiler():
#         links = re.compile(url_pattern).findall(txt)
#         for single_link in links:
#             if single_link.find(playlist_pattern) > -1:
#                 return single_link

# get_link()
"""
def get_single_serial_data(url, only_last_episode=True):
    all_serial_episodes = []
    last_serial_episode = []
    if type(url) is str:
        serial_data = ast.literal_eval(urllib.urlopen(url).read())
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
    elif type(url) is list:
        raise TypeError('url must be <str>, got %s. Consider using "get_multiple_serials_data" method.' % type(url))


def get_multiple_serials_data(urls, only_last_episode=True):
    all_serials_episodes = []
    if type(urls) is list:
        for url in urls:
            serial_episodes = get_single_serial_data(url, only_last_episode)
            all_serials_episodes += serial_episodes
    elif type(urls) is str:
        raise TypeError('urls must be <list>, got %s. Consider using "get_single_serial_data" method.' % type(urls))
    else:
        raise TypeError('urls must be <list>, got %s' % type(urls))
    return all_serials_episodes

url1 = 'http://www.online-life.me/pls3/67b0b864981feee48ac0b5da857621e9/qqeWm6Wpl5GdmLOknJujo5yRmd3x65Pb7eqfjw/pl_brooklyn.9-9.2013_all_s.txt&st=22AOOAuB7DbZVeNzIQNzSx13L0LGZf1cYkhv3W6z95TLiwZN1wWNF3njAXSLdMwLd1wZrD'
url2 = 'http://www.online-life.me/pls3/65a4c18ad0d850fb9ab4cef02bb7baa4/qqeWm6WqlpOemLOknJujo5yRmd3x65Pb7eqfjw/pl_belyi_vorotnichok_all_s.txt&st=22AOOAuB7DbZVeNzIQNzSx13L0LGZf1cYkhv3W6z95TLiwZN1wWNF3njAXSLdMwLd1wZrD'
urls = [url1, url2]
# print get_multiple_serials_data(url1)
print get_multiple_serials_data('azaza')

def xml_track_factory(episodes):
    _now = datetime.datetime.now()
    # cur_date = _now.year + _now.month + _now.day
    # cur_time = _now.hour + _now.minute + _now.second
    # name_xmlns = u'xmlns'
    # val_xmlns = u'http://xspf.org/ns/0/'
    # name_xmlns_vlc = u'vlc'
    # val_name_xmlns_vlc = u'http://www.videolan.org/vlc/playlist/ns/0/'
    # name_version = u'version'
    # val_version = u'1'
    playlist_path = 'd:\\PROJECTS\\github\\neverless-to-test\\parsing\\data\\'  # todo configurable or from some object
    playlist_name = str(datetime.datetime.now().second) + '.xspf'
    xml_playlist = etree.Element('playlist')
    # xml_playlist.set(name_xmlns, val_xmlns)
    # xml_playlist.set(name_xmlns + ":" + name_xmlns_vlc, val_name_xmlns_vlc)
    # xml_playlist.set(name_version, val_version)
    xml_title_playlist = etree.SubElement(xml_playlist, 'title')
    # xml_title_playlist.text = 'Playlist %s-%s-%s %s:%s:%s' % (_now.year, _now.month, _now.day, _now.hour, _now.minute, _now.second)
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

    # for i in range(0, 3):
    # xml_track_tracklist = etree.SubElement(xml_tracklist_playlist, 'track')
    #     xml_location_track = etree.SubElement(xml_track_tracklist, 'location')
    #     xml_location_track.text = 'some http'
    #     xml_title_track = etree.SubElement(xml_track_tracklist, 'title')
    #     xml_title_track.text = 'some title here'
    # playlist_file = open(playlist_path, 'w+')
    # output = playlist_file.write(etree.tostring(xml_playlist, pretty_print=True, encoding='utf-8'))
    # playlist_file.close()
    return output



def test_fact(episodes):
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


list_of_lists = []
list_one = ['2', '2']
list_two = ['3', '3']
list_of_lists.append(list_one)
list_of_lists.append(list_two)
print test_fact(list_of_lists)

# def create_file():
# path = 'd:\\PROJECTS\\github\\neverless-to-test\\parsing\\data\\'
# name = str(datetime.datetime.now().second) + '.xspf'
#     return open(path + name, 'w').close()
#
# print etree.tostring(xml_playlist, pretty_print=True)
#
# xhtml = etree.Element('tatata', "{http://www.w3.org/1999/xhtml}vlc")
# # body = etree.SubElement(xhtml, "{http://www.w3.org/1999/xhtml}body")
# # body.text = "Hello World"
# print xml_track_factory(1, 1)
# xml_file = 'd:\\PROJECTS\\github\\neverless-to-test\\parsing\\data\\123123.xspf'
# playlist = open(xml_file)
# playlist_data = playlist.read()
# tree = etree.parse(xml_file)
# print etree.tostring(etree.fromstring(playlist_data))
# root = tree.getroot()
# chacha = root[1]
# new_track = etree.SubElement(chacha, 'track')
# track_location = etree.SubElement(new_track, 'location')
# track_location.text = 'location_text'
# track_title = etree.SubElement(new_track, 'title')
# track_title.text = 'title_test'
# track_duration = etree.SubElement(new_track, 'duration')
# track_duration.text = 'duration_text'
# # print etree.tostring(track_title)
# xml1_file = 'd:\\PROJECTS\\github\\neverless-to-test\\parsing\\data\\222.xspf'
# new_xml_file = open(xml1_file, 'w')
# b = etree.tostring(root, pretty_print=True, encoding='utf-8')
# new_xml_file.write(b)
# new_xml_file.close()
# print 'tratata'

# playlist.close()

# child = root.getchildren()
# print child
# for ch in child:
#     print ch.getchildren()
#     for c in ch:
#         print c.getchildren()



# for child in root:
#     for el in child:
#         print el.tag, el.attrib
# for track in root.findall('track'):
#     print track
# location = track.find('location').text
# title = track.get('title')
# print title, location
# xml_file.close()


# xml_file.close()
# soup = BeautifulStoneSoup(playlist)
# trackList_tag = Tag(soup, 'tracklist')
# track_tag = Tag(soup, 'track')
# track_tag.insert(0, track_tag)
# text = NavigableString('SampleText')
# track_tag.insert(0, text)
# print soup.prettify()

# soup = BeautifulStoneSoup()
# tag0 = Tag(soup, 'tag0')
# tag1 = Tag(soup, 'tag1')
# tag2 = Tag(soup, 'tag2')
#
# soup.insert(0, tag0)
# tag0.insert(0, tag1)
# tag1.insert(0, tag2)
# print soup.prettify()
"""