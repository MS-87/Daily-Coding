'''
Easy - sqrtx
https://leetcode.com/problems/sqrtx/

Given a non-negative integer x, compute and return the square root of x.
Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.
'''

#Easiest solution
import math
class Solution:
    def mySqrtEZ(self, x: int) -> int:
        return int(sqrt(x))


#Fastest solution - Binary search
    def mySqrtFast(self, x):

        lo, hi = 0, x

        while lo <= hi:

            #Find the mid point between lo and high
            mid = (lo + hi) // 2
            
            #If the square of both numbers:

            #Is bigger than x, then the answer is between lo and mid
            if mid * mid > x:
                hi = mid - 1

            #Is smaller than x, then the answer is between mid and high
            elif mid * mid < x:
                lo = mid + 1

            #exact, then you found the right answer
            else:
                return mid
        
        # When there is no perfect square, hi is the the value on the left
        # of where it would have been (rounding down). If we were rounding up, 
        # we would return lo
        return hi