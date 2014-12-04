# coding=utf-8
from BeautifulSoup import BeautifulStoneSoup, Tag, NavigableString     # Для обработки XML

xml_file = open('f:\\123123.xspf')
playlist = xml_file.read()
# xml_file.close()
soup = BeautifulStoneSoup(playlist)
trackList_tag = Tag(soup, 'tracklist')
track_tag = Tag(soup, 'track')
track_tag.insert(0, track_tag)
text = NavigableString('SampleText')
track_tag.insert(0, text)
print soup.prettify()

# soup = BeautifulStoneSoup()
# tag0 = Tag(soup, 'tag0')
# tag1 = Tag(soup, 'tag1')
# tag2 = Tag(soup, 'tag2')
#
# soup.insert(0, tag0)
# tag0.insert(0, tag1)
# tag1.insert(0, tag2)
# print soup.prettify()