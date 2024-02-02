from PIL import Image

im1=Image.open("D:\\Python\\练习和考试题\\图像处理\\picframe59.png")
r,g,b =im1.split()
newg=g.point(lambda i:i*0.9)#将g通道的颜色变为原来的0.9倍
newb=b.point(lambda i:i<100)#选择b通道值低于100的像素点
om=Image.merge(im1.mode,(r,newg,newb))
om.save("D:\\Python\\练习和考试题\\图像处理\\picframe59NewRGB.png")


'''Image.point(func) 根据函数func的功能对每一个元素进行运算，返回图片副本
Image.split() 提取RGB的图像的每一个颜色通道，返回图像副本
Image.merge(mode,bands) 合并通道，其中mode表示色彩，bands表示新的色彩通道
Image.blend(im1,im2,alpha) 将两幅图片im1和im2按照如下公式插值后生成新的图片:im1*(1.0-alpha)+im2*alpha
'''
