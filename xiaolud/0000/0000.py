# coding=utf-8

from PIL import Image,ImageDraw,ImageFont

# 加载图片信息
image_content = Image.open('weChat_avatar.png')

# 加载字体信息并定义字体坐标
font_content  = ImageFont.truetype('ahronbd.ttf', 30)

font_width = image_content.size[0] - image_content.size[0]/10
font_high = image_content.size[1]/10

# 添加计数信息
draw_instance = ImageDraw.Draw(image_content)
draw_instance.text((font_width, font_high), '4', (255,0,0), font = font_content)
image_content.show()
image_content.save('weChat_avatar_modify.png')
