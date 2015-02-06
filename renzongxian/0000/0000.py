# Source:https://github.com/Show-Me-the-Code/show-me-the-code
# Author:renzongxian
# Date:2014-11-30
# Python 3.4
# coding=utf-8

from PIL import Image, ImageDraw, ImageFont
import sys


def add_num_to_img(file_path):
    im = Image.open(file_path)
    im_draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("arial.ttf", int(im.size[0]/5))
    im_draw.text((int(im.size[0]-im.size[0]/10), 5), "4", (256, 0, 0), font=font)
    del im_draw
    im.save('./result.png')

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Need at least 1 parameter. Try to execute 'python 0000.py $image_path'")
    else:
        for infile in sys.argv[1:]:
            try:
                add_num_to_img(infile)
                print("Success!")
            except IOError:
                print("Can't open image!")
                pass

