# -*- coding: utf-8 -*-
from PIL import Image, ImageFont, ImageDraw
import time, sys
from io import BytesIO

reload(sys)
sys.setdefaultencoding('utf-8')

try:
    import cStringIO as StringIO
except ImportError:
    import StringIO


def get_qr_pic(qr_token):
    pass


def generate_sharing_pic(to_text, audio_time, from_text, qr_token, pic=None):
    """
    生成分享图片
    :param to_text: str, like 'TO：阿根廷队'
    :param audio_time: int, no more than 15
    :param from_text: set, user set
    :param qr_token: TODO: needed to generate QR code
    :param pic: StringIO or fp, default is world cup logo
    :return: StringIO, pic
    """
    audio_time = 15 if audio_time > 15 else audio_time
    qr_pic = get_qr_pic(qr_token)
    pass


class SharingPicGenerator(object):

    def __init__(self, background_fp):
        self.bk_im = Image.open(background_fp).convert()
        self.paste_list = []
        self.text_list = []
        self.bk_im.save('string_io_out.png')

    def add_paste_task(self, pic_fp, region_box):
        """

        :param pic_fp: anything can be opened by Image.open()
        :param region_box: tuple of for lines
        :return:
        """
        pic_foo = Image.open(pic_fp)

        width = region_box[2] - region_box[0]
        height = region_box[3] - region_box[1]
        region = pic_foo.resize((width, height), Image.ANTIALIAS)

        self.paste_list.append(tuple([region, region_box]))

    def __do_paste(self):
        for task in self.paste_list:
            self.bk_im.paste(task[0], task[1])

    def add_text_task(self, text, text_xy, *font_args):
        print text
        _font = ImageFont.truetype(*font_args)
        self.text_list.append(tuple([text_xy, unicode(text), _font]))

    def __add_text(self):

        draw = ImageDraw.Draw(self.bk_im)
        for task in self.text_list:
            draw.text(xy=task[0], text=task[1], font=task[2])  # 这里需要改进

    def generate(self):
        self.__do_paste()
        self.__add_text()
        rs = BytesIO()
        self.bk_im.save(rs, format='PNG')
        return rs


if __name__ == '__main__':
    with open('/Users/hector/PycharmProjects/qingting/sharing_pic_generator/assets/Group 2 Copy.png', 'rb') as f_in:
        tmp = f_in.read()

    io_t = BytesIO()
    io_t.write(tmp)
    tmp_foo = SharingPicGenerator(io_t)

    tmp_foo.add_paste_task('assets/结束录音@3x.png', (210, 210, 330, 330))
    import emoji

    tmp_foo.add_text_task(emoji.emojize(u'这里supposed有一个emoji——>:grinning_face:<-'), (100,400), "/Users/hector/PycharmProjects/qingting/sharing_pic_generator/PingFang.ttc", 40)
    tmp_foo.add_text_task(u"\U0001f300", (400,400), "/Users/hector/PycharmProjects/qingting/sharing_pic_generator/PingFang.ttc", 40)
    # # u"\U0001f300"
    # Phoebe🎄🎄

    with open('out_test_pingfang.png', 'wb') as f_o:
        f_o.write(tmp_foo.generate().getvalue())
