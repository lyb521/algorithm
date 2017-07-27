# -*- coding: utf-8 -*-
# @Created by PyCharm Community Edition.
# @User: leiyongbo <lyb19900227@126.com>
# @Date: 2017/7/27
# @Time: 09:59
# @url: http://www.lintcode.com/zh-cn/problem/rectangle-area/
# @Description:
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height


    def getArea(self):
        return self.width * self.height
if __name__ == '__main__':
    rec =  Rectangle(3, 4)
    print (rec.getArea())