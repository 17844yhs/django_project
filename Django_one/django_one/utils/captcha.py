import random
import string

def random_str(length=4):
  """ 随机字符串 默认长度 4
   :param length: 默认长度 4
   :return:
   """
  
  return ''.join(random.sample(string.ascii_letters, length))


# 生成颜色
def random_color():
  # RGB
  return random.randint(0,255),random.randint(0,255),random.randint(0,255)

#生成验证码
import os

from PIL import Image, ImageDraw, ImageFont, ImageFilter
# 生成验证码
def generate_captcha(width=160,height=40,length=4):
  # 创建一个空白图片
  image = Image.new('RGB',(width,height),color=(255,255,255))
  # 获取画布里的内容
  code = random_str()
  # 获取画笔
  draw = ImageDraw.Draw(image)
  # 随机颜色的填充
  for x in range(0,width,2):  # 从 x=0 开始，以步长 2 遍历到 width
    for y in range(height):   # 对于每个 y 值（从 0 到 height）
      draw.point((x,y),fill=random_color()) 
  # 获取字体
  font = ImageFont.truetype(os.path.join(os.path.dirname(__file__),'STHUPO.TTF'),size=30)
  # 将内容写入图片
  for t in range(length):
    # 通过画笔工具写入内容
    # ; 这是文本绘制位置的坐标 (x, y)。 x 坐标是通过 (40 * t + 5) 计算得出的，表示文本在水平位置的偏移。t 是循环的变量，通常表示文本字符的索引，意味着文本的水平位置会根据 t 逐渐变化，形成一个水平的排列效果。
    # ; y 坐标是固定的 5，表示文本的垂直位置，从顶部向下偏移 5 像素。
    draw.text((40*t+5,5),code[t],font=font,fill=random_color())  
  # 图片的模糊
  image = image.filter(ImageFilter.BLUR)
  # 返回图片，验证码
  return image,code

if __name__ == '__main__':
  # random_str()
  img ,code = generate_captcha()
  # img.save('code.png')
  img.save(os.path.join('django_one/static/imgs','code.png'))
  # img.save('code.png') 是使用 Pillow 库将图像保存为文件。
  print(code)
  # print(os.path.dirname(__file__))