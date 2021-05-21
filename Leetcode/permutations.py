'''
Medium - Permutations
https://leetcode.com/problems/permutations/

Given an array nums of distinct integers, return all the possible permutations. 
You can return the answer in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
'''


'''
My Solution - 
Just permutate the whole thing
'''

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.masterList = []
        self.deepermute(nums, []) #Call first iteration of deepermute
        print(self.masterList)
        return(self.masterList)

    def deepermute(self, remaining, current = []):
        '''this function uses recursion to call a smaller chunk of the list each time'''
        #If we have reached the last digit, just append it, and return
        if len(remaining) == 1:
            current.append(remaining[0])
            self.masterList.append(current)
            return

        else:
            #For every digit, call deepermute with a new list without said digit
            for digit in remaining:
                #Could optimize this?
                temp = list(remaining)
                temp.remove(digit)

                temp2 = list(current)
                temp2.append(digit)
                self.deepermute(temp, temp2)