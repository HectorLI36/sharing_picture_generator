#声音明信片-分享图片生成器

##说明
本组件基于Pillow==5.1.0开发，支持中文英文，支持自定图片，支持自定字体。



##使用方法
1.开始
>from PicGenerator import SharingPicGenerator as Generator
>
2.初始化,导入背景图片。传入背景图片参数为文件路径或BytesIO类型。w,h分别为背景图片的宽度和高度。
>pic_foo = Generator(_background_fp_, w, h)
>
3.添加粘贴图片任务。
>pic_foo.add_paste_task(_pasted_pic_fp_, _region_box_)

参数：
1. pasted_pic_fp：文件路径或BytesIO
2. region_box:包含四个整数的tuple.图片在背景图片上的四个边距背景图片左边（竖线）或上边（横线）的像素距离,按顺序为左、上、右、下的位置。
eg：(210, 210, 330, 330)
>tmp_foo.add_paste_task('sharing_pic_generator/common/default_photo.png', (210, 210, 330, 330))
>
说明：图片在粘贴之前会进行resize，会导致图片比例发生变化，建议裁剪后调用。

4.添加文字任务
>pic_foo.add_text_task(_text_args_, _*font_args_)
>
参数：

_text_args_: dict,text为unicode类型，algin为对齐模式，支持left，center，right模式。
xy：包含两个整数的tuple。
1. 对于algin = left：x,y文本框左上角距离左边和上边的距离
2. 对于algin = center：x无所谓，y为文本框上边离背景图片上沿的像素距离
3. 对于algin = right：x为文本框**右边**距离背景图片左边的像素距离，y为文本框上边离背景图片上沿的像素距离


eg：<br>
>text_args = {'text': u'测试文字', 'xy': (0, 75), 'align': 'center'}
>
_font_args_:可根据Pillow的要求任意添加，必须包含字体的路径，文本大小(前两个参数)

eg：
>pic_foo.add_text_task(text_args, 'common/assets/PingFang.ttc', 28)

5.生成图片：
>pic_foo.generate()
>
返回值为BytesIO类型


6.进阶

可将参数统一写到一个.py或.json文件中，以免