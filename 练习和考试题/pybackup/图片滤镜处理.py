from PIL import Image
from PIL import ImageFilter

im1=Image.open("D:\\Python\\练习和考试题\\图像处理\\picframe59.png")
om=im1.filter(ImageFilter.EMBOSS)#滤镜方法
'''ImageFilter.BLUR 图像模糊处理
ImageFilter.CONTOUR 图像轮廓效果
ImageFilter.DETAIL  图像细节效果
ImageFilter.EDGE_ENHANCE 图像边界加强
ImageFilter.EDGE_ENHANCE_MORE 图像阈值边界加强
ImageFilter.EMBOSS      图像浮雕效果
ImageFilter.FIND_EDGES  图像边界效果
ImageFilter.SMOOTH      图像平滑效果
ImageFilter.SMOOTH_MORE 图像阈值平滑效果
ImageFilter.SHARPEN     图像锐化效果'''

om.save("D:\\Python\\练习和考试题\\图像处理\\picframe59EMBOSS.png")