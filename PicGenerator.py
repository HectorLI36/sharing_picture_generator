# -*- coding: utf-8 -*-
from PIL import Image, ImageFont, ImageDraw
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
import time, sys
from io import BytesIO

reload(sys)
sys.setdefaultencoding('utf-8')

try:
    import cStringIO as StringIO
except ImportError:
    import StringIO
import pic_config

W, H = pic_config.BACKGROUND_W, pic_config.BACKGROUND_H


class SharingPicGenerator(object):

    def __init__(self, background_fp, w, h):
        self.bk_im = Image.open(background_fp).convert()
        self.paste_list = []
        self.text_list = []
        self.w = w
        self.h = h
        self.bk_im.save('string_io_out.png')

    def add_paste_task(self, pic_fp, region_box, mask=None):
        """

        :param mask:
        :param pic_fp: anything can be opened by Image.open()
        :param region_box: tuple of for lines
        :return:
        """
        pic_foo = Image.open(pic_fp)

        width = region_box[2] - region_box[0]
        height = region_box[3] - region_box[1]
        resized_pic = pic_foo.resize((width, height), Image.ANTIALIAS)
        if mask:
            resized_pic.putalpha(255)
            self.paste_list.append(tuple([resized_pic, region_box, resized_pic]))  # 【-1】有问题
        else:
            self.paste_list.append(tuple([resized_pic, region_box, None]))

    def __do_paste(self):
        for task in self.paste_list:
            self.bk_im.paste(task[0], task[1], task[2])

    def add_text_task(self, text_args, *font_args):
        """
        中文必须是Unicode
        如果是向右对其的，需要xy是右上角的点，x是最右边距离左边框的像素数
        :param text_args:
        :param font_args:
        :return:
        """
        _font = ImageFont.truetype(*font_args, index=text_args['index'])
        draw = ImageDraw.Draw(self.bk_im)
        if text_args['align'] == 'center':
            # w, h = _font.getsize(text_args['text'])
            # os = _font.getoffset(text_args['text'])
            w, h = draw.textsize(text_args['text'], font=_font)
            # w0 = len(text_args['text']) * font_args[-1]
            new_xy = ((W - w) / 2, text_args['xy'][-1])
            self.text_list.append(tuple([new_xy, unicode(text_args['text']), _font]))

        elif text_args['align'] == 'right':
            # 由右上角计算出左上角
            w, h = draw.textsize(text_args['text'], font=_font)
            new_xy = ((text_args['xy'][0] - w), text_args['xy'][-1])
            self.text_list.append(tuple([new_xy, unicode(text_args['text']), _font]))
        else:

            self.text_list.append(tuple([text_args['xy'], unicode(text_args['text']), _font]))

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
    with open('/Users/hector/PycharmProjects/qingting/sharing_pic_generator/common/worldcup_background.png',
              'rb') as f_in:
        tmp = f_in.read()

    io_t = BytesIO()
    io_t.write(tmp)
    tmp_foo = SharingPicGenerator(io_t)

    tmp_foo.add_paste_task('/Users/hector/PycharmProjects/qingting/sharing_pic_generator/common/default_photo.png', (210, 210, 330, 330))
    # import emoji

    text_args = {'text': u'测试', 'xy': (0, 75), 'align': 'center'}
    tmp_foo.add_text_task(text_args, "/Users/hector/PycharmProjects/qingting/fifa_generate_pic_test/苹方黑体-准-简.ttf", 45)
    text_args = {'text': u'测试', 'xy': (W - 102, 544), 'align': 'right'}
    tmp_foo.add_text_task(text_args, "/Users/hector/PycharmProjects/qingting/fifa_generate_pic_test/苹方黑体-准-简.ttf", 28)

    # tmp_foo.add_text_task(u"\U0001f300", (400,400), "/Users/hector/PycharmProjects/qingting/sharing_pic_generator/PingFang.ttc", 40)
    # # u"\U0001f300"
    # Phoebe🎄🎄

    with open('out_test_pingfang_2.png', 'wb') as f_o:
        f_o.write(tmp_foo.generate().getvalue())
