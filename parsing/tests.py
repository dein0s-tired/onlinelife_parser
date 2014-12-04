
__author__ = 'dein0s'

import urllib
import ast
import re

# url = 'http://www.online-life.me/pls3/de67ee4c2e8f4ce145538fc90015d334/qqeWmq2rm5igmrOknJujo5yRmd3x65Pb7eqfjw/pl_grimm_all_s.txt&st=22AOOAuB7DbZVeNzIQNzSx13L0LGZf1cYkhv3W6z95TLiwZN1wWNF3njAXSLdMwLd1wZrD'

def get_link():
    # url = 'http://www.online-life.me/4423-morskaya-policiya-novyy-orlean-2014.html'
    # <type 'dict'> - serial_data, <type 'list'> - serial_data[playlist], <type 'dict'> - serial_data[playlist][0], ['comment', 'download', 'file'] - keys for last dict
    # url = 'http://www.online-life.me/277-hodyachie-mertvecy-online-all-seasons.html'
    # <type 'dict'> - serial_data, <type 'list'> - serial_data[playlist], <type 'dict'> - serial_data[playlist][0], ['comment', 'playlist'] - keys for last dict
    url = 'http://www.online-life.me/2377-bruklin-9-9-2013.html'
    url_pattern = r'https?://[^\s<>"]+'
    playlist_pattern = 'all_s.txt'
    txt = urllib.urlopen(url).read()
    # a_data = ast.literal_eval(txt)
    links = re.compile(url_pattern).findall(txt)
    for single_link in links:
        if single_link.find(playlist_pattern) > -1:
            return single_link
        else:
            pass

# playlist_link = get_link()

def get_serial_info(link):
    files = []
    names = []
    last_position = None
    serial_data = ast.literal_eval(urllib.urlopen(link).read())
    if 'playlist' not in serial_data['playlist'][0].keys():  # one season
        season = serial_data['playlist']
        last_position = len(season) - 1
        for episode in season:
            files.append(episode['file'])
            names.append(episode['comment'])
    else:
        seasons = serial_data['playlist']
        for season in seasons:
            episodes = season['playlist']
            last_position = len(episodes) - 1
            for episode in episodes:
                files.append(episode['file'])
                names.append(episode['comment'])
    print names[len(names)-1], files[len(files)-1]

    # print '%s - serial_data, %s - serial_data[playlist], %s - serial_data[playlist][0], %s - keys for last dict' % (type(serial_data), type(serial_data['playlist']), type(serial_data['playlist'][0]), serial_data['playlist'][0].keys())
    # seasons = serial_data['playlist']
    # if seasons[0]:
    #     return 'more then 1 season'
    # else:
    #     return 'only one season'
    #     for season in seasons:
    #         episodes = season['playlist']
    #         for episode in episodes:
    #             return episode['comment']

print get_serial_info(get_link())
# comm = a_data['playlist'][0]['playlist'][00]['comment']
# file = a_data['playlist'][0]['playlist'][00]['file']
#
# seasons = a_data['playlist']
# if len(seasons) > 1:
#     for season in seasons:
#         # print "%s episodes in %s season" % (len(season['playlist']), season['comment'])
#         episodes = season['playlist']
#         for episode in episodes:
#             print episode['comment']
#             # print '%s episode of %s in %s season with comment %s' % (episode, len(season['playlist']), season['comment'], episode['comment'])
