# -*- coding: utf-8 -*-
# @Created by PyCharm Community Edition.
# @User: leiyongbo <lyb19900227@126.com>
# @Date: 2017/5/25
# @Time: 15:08
# @Description:单例模式

class Singleton(object):

    # 定义静态变量实例
    __singleton = None

    def __init__(self):
        pass

    @staticmethod
    def getInstance():
        if Singleton.__singleton is None:
            Singleton.__singleton = Singleton()
            print '实例化单例'
        return Singleton.__singleton


if __name__ == '__main__':
    Solution = Singleton()

    Solution.getInstance()
    Solution.getInstance()