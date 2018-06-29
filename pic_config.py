# coding=utf-8
# DO NOT MAKE CHANGES!
BACKGROUND_PIC_FP = 'common/assets/worldcup_background.png'
DEFAULT_MAIN_FP = 'common/assets/new_default.png'
DEFAULT_FONT = 'common/assets/PingFang.ttc'

SLOGAN = u'我为{}声援！你敢进来点赞吗？'  # type: unicode
TO = u'TO：{}'

PIC_LOCATIONS = {
        'main': (118, 412, 298, 646),
        'qr_code': (56, 814, 176, 934)
    }

BACKGROUND_W = 750
BACKGROUND_H = 968
DEFAULT_FONT_INDEX = 5

TEXT_LOCATIONS = {
    'title': {'text': '', 'xy': (0, 75), 'align': 'center'},
    'slogan': {'text': '', 'xy': (0, 146), 'align': 'center', 'index': 2},
    'to': {'text': '', 'xy': (118, 320), 'align': 'left'},
    'duration': {'text': '', 'xy': (BACKGROUND_W - 172, 448), 'align': 'right'},
    'from': {'text': '', 'xy': (BACKGROUND_W - 102, 544), 'align': 'right'},
    'date': {'text': '', 'xy': (BACKGROUND_W - 102, 600), 'align': 'right'}
}


"""
0-PingFang HK-Regular
1-PingFang TC-Regular
2-PingFang SC-Regular
3-PingFang HK-Medium
4-PingFang TC-Medium
5-PingFang SC-Medium
6-PingFang HK-Semibold
7-PingFang TC-Semibold
8-PingFang SC-Semibold
9-PingFang HK-Light
10-PingFang TC-Light
11-PingFang SC-Light
12-PingFang HK-Thin
13-PingFang TC-Thin
14-PingFang SC-Thin
15-PingFang HK-Ultralight
16-PingFang TC-Ultralight
17-PingFang SC-Ultralight
"""