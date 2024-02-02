from PIL import Image
from PIL import ImageEnhance

im1=Image.open("D:\\Python\\练习和考试题\\图像处理\\picframe59.png")
om=ImageEnhance.Contrast(im1)
om.enhance(20).save("D:\\Python\\练习和考试题\\图像处理\\picframe59Contrast.png")

'''ImageEnhance.enhance(factor) 对选取的属性的数值增强factor倍
ImageEnhance.Color(im)       调整图像的颜色平衡
ImageEnhance.Contrast(im)    调整图像的对比度
ImageEnhance.Brightness(im)  调整图像的亮度
ImageEnhance.Sharpness(im)   调整图像的锐度'''