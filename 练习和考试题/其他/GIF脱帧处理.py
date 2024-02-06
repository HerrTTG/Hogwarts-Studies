from PIL import Image
im = Image.open('D:\\Python\\练习和考试题\\脱帧图片\\640.gif')      # 读入一个GIF文件
try:
    im.save('D:\\Python\\练习和考试题\\脱帧图片\\picframe{:02d}.png'.format(im.tell()))
    while True:
        im.seek(im.tell()+1)
        im.save('D:\\Python\\练习和考试题\\脱帧图片\\640\\picframe{:02d}.png'.format(im.tell()))
except:
    print("处理结束")