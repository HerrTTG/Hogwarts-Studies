'''
作业要求
编写一个Python程序，创建一个几何图形计算程序，使用静态方法来计算矩形的面积和周长。
'''

class Rectangle:
    @staticmethod
    def get_area(width,height):
        return width*height

    @staticmethod
    def get_circle(width,height):
        return  2 * (width+height)



if __name__=='__main__':
    print('矩形的面积为:{0}，矩形的周长为{1}'.format(Rectangle.get_area(100,200) \
                                                    ,Rectangle.get_circle(100,200)))