'''
Easy - Two Sum
https://leetcode.com/problems/two-sum/

Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
'''

#O[n] solution
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        print(nums)
        
        iterArr = {}
        
        for i, x in enumerate(nums):
            
            if target - x in iterArr:
                v1 = i
                v2 = iterArr.get(target-x)
                return(v1, v2)

                
            else:
                iterArr[x] = i

'''
Explanation:
https://www.techiedelight.com/find-pair-with-given-sum-array/
'''