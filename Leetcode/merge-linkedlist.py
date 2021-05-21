'''
Easy - Merge two sorted lists
https://leetcode.com/problems/merge-two-sorted-lists/

Merge two sorted linked lists and return it as a sorted list. 
The list should be made by splicing together the nodes of the first two lists.
'''

'''My solution:
    Just check and add to a third list'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        if l1 == [] and l2 == []:
            return []
        elif l1 == []:
            return l2
        elif l2 == []:
            return l1
        
        #l3 is first element
        l3 = ListNode()
        index = l3
        
        while l1 or l2:
            
            #If both have reached "None", we're done
            if l1 == None and l2 == None:
                break
            
            #If one is None, just add the rest to l3 and call it a day
            elif l1 == None or l2 == None:
                index = self.completeList(l1 or l2, index)
                break
            
            if l1.val > l2.val:
                index = self.addElement(l2.val, index)
                l2 = l2.next
                
            elif l1.val < l2.val: 
                index = self.addElement(l1.val, index)
                l1 = l1.next
                
            #l1 == l2
            else:
                index = self.addElement(l1.val, index)
                index = self.addElement(l2.val, index)
                l2 = l2.next
                l1 = l1.next
                
        return l3.next
    
    def addElement(self, value, index):
        
        newl = ListNode(val = value)
        index.next = newl
        index = newl
        return index
    
    def completeList(self, lx, index):
        
        if lx != None:
            index = self.addElement(lx.val, index)
            index = self.completeList(lx.next, index)
            
        return index

#Super clever solution someone did
#Basically use the existing list and keep appending to the smaller one
#Keep swithicng between a, b = b, a as needed.

class Solution2:
    def mergeTwoLists(self, a, b):
        if a and b:
            if a.val > b.val:
                a, b = b, a
            a.next = self.mergeTwoLists(a.next, b)
        return a or b

#Much cleaner version of my algo
#You never have to touch values, you are just assigning the nodes that
#already exist in l1 and l2 to your index (in this case cur)
# iteratively
def mergeTwoLists1(self, l1, l2):
    dummy = cur = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next