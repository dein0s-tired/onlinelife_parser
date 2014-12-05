# coding=utf-8
from lxml import etree
import datetime


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


list_of_lists = []
list_one = [2, 2]
list_two = [3, 3]
list_of_lists.append(list_one)
list_of_lists.append(list_two)
# print xml_track_factory(list_of_lists)

# def create_file():
# path = 'd:\\PROJECTS\\github\\neverless-to-test\\parsing\\data\\'
#     name = str(datetime.datetime.now().second) + '.xspf'
#     return open(path + name, 'w').close()
#
print xml_track_factory(list_of_lists)
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