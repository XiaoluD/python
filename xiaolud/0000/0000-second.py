# coding=utf-8

from PIL import Image,ImageDraw,ImageFont


def img_font_content(img):

    image_content = Image.open(img)
    # 定义图片坐标
    font_width = image_content.size[0] - image_content.size[0]/10
    font_high = image_content.size[1]/10
    return (image_content,font_width,font_high)


def img_modify(img_font_content):

    image_content,font_width,font_high = img_font_content
    # 定义字体
    font_content  = ImageFont.truetype('ahronbd.ttf', 30)
    # 修改并保存
    draw_instance = ImageDraw.Draw(image_content)
    draw_instance.text((font_width, font_high), '4', (255,0,0), font = font_content)
    image_content.show()
    image_content.save('weChat_avatar_modify.png')

def main():

    pre_img = img_font_content('weChat_avatar.png')
    end_img = img_modify(pre_img)


if __name__ == '__main__':
    main()