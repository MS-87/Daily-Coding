'''
Easy - reverse Integer
https://leetcode.com/problems/two-sum/

Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
'''

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        #Convert to string, treat as array, reverse by ::-1
        y = str(x)[::-1]
        
        #Check to see if the negative is now at the end, if it is, put it in the beggining
        if y[-1] == '-':
            y = '-' + y[:-1]
        
        #Check size bounds
        num = int(y)
        if (num > 2147483647) or (num < -2147483647):
            num = 0
        
        return (num)