# -*- coding:utf-8 -*-

import os
import sys

import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


# 设置文字水印
def set_water_text(imagefile, text):
    img = Image.open(imagefile)
    (img_x, img_y) = img.size

    # 文字字体像素高度为图片高度的 1/20
    # ttfont = ImageFont.truetype('/work/html/cool_python/edit_photo/huakangdianjinti.TTC', int(img_y / 20))
    ttfont = ImageFont.truetype('/work/html/cool_python/edit_photo/pangtouyu.ttf', int(img_y / 20))
    #font color
    fillColor="#000000"
    draw = ImageDraw.Draw(img)
    draw.text((int(img_x / 20), img_y - int((img_y * 1.3) / 20)),text, font=ttfont,fill=fillColor)

    newdir = "new"
    if not os.path.exists(newdir):
        os.mkdir(newdir)

    img.save(newdir + '/' + text + '.png', 'png')


if __name__ == '__main__':
    files = os.listdir(os.getcwd())
    for filename in files:
        if 'jpg' == filename.split('.')[-1].lower() or 'png' == filename.split('.')[-1].lower():
            texts=('李白',
                   '张宇',
                   )
            for text in texts:
                set_water_text(filename, text)
                print(text)