# -*- coding: utf-8 -*-
# @Created by PyCharm Community Edition.
# @User: leiyongbo <lyb19900227@126.com>
# @Date: 2017/8/9
# @Time: 16:52
# @url: http://www.lintcode.com/zh-cn/problem/longest-substring-without-repeating-characters/#
# @Description:给定一个字符串，请找出其中无重复字符的最长子字符串。


class Solution:
    # @param s: a string
    # @return: an integer
    def lengthOfLongestSubstring(self, s):
        # write your code here
        new_s_list = []
        max_lenth = 0
        for i in range(0, len(s)):
            if s[i] not in new_s_list:
                new_s_list.append(s[i])
            else:
                #该位置之前的都丢弃
                new_s_list = new_s_list[new_s_list.index(s[i])+1:]
                new_s_list.append(s[i])
            if len(new_s_list) > max_lenth:
                max_lenth = len(new_s_list)
        return max_lenth


if __name__ == '__main__':
    s = Solution()
    print (s.lengthOfLongestSubstring("gehmbfqmozbpripibusbezagafqtypz"))