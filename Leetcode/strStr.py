'''
Easy - strStr()
https://leetcode.com/problems/implement-strstr/

Return the index of the first occurrence of needle in haystack, 
or -1 if needle is not part of haystack.
'''

#trivial solution
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)