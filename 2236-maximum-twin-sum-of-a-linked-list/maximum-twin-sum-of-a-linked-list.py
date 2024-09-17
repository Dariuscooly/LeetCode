# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        lst_values = []
        retval = 0
        curr = head
        while curr:
            temp = curr.val
            lst_values.append(temp)
            curr = curr.next
        
        left , right = 0 , len(lst_values) - 1

        while left < right:
            temp = lst_values[left] + lst_values[right]
            retval = max(retval , temp)
            left += 1
            right -= 1
        return retval