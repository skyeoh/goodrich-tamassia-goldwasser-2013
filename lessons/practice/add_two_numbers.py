"""
Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero,
except the number 0 itself.

Example:
    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#Function to populate singly-linked list
def populate_list(nums):
    """
    :type nums: List[int]
    :rtype: ListNode
    """
    size = len(nums)
    next = None
    for i in range(size):
        next = ListNode(nums[i], next)
    return next

#Function to output elements of singly-linked list
def output_list(l):
    """
    :type l: ListNode
    """
    next = l
    while next != None:
        print(next.val)
        next = next.next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        next1 = l1
        next2 = l2
        val = 0
        temp = []
        while next1 != None or next2 != None:
            if next1 == None:
                val = next2.val + val // 10
                next2 = next2.next
            elif next2 == None:
                val = next1.val + val // 10
                next1 = next1.next
            else:
                val = next1.val + next2.val + val // 10
                next1 = next1.next
                next2 = next2.next
            temp.insert(0, val % 10)
        if val >= 10:
            temp.insert(0, 1)
        return populate_list(temp)

if __name__ == '__main__':
    test = Solution()

    # Test 0: From example above
    print()
    num1 = [3, 4, 2]
    l1 = populate_list(num1)
    output_list(l1)

    print('+')
    num2 = [4, 6, 5]
    l2 = populate_list(num2)
    output_list(l2)

    print('=')
    output_list(test.addTwoNumbers(l1, l2))

    # Test 1: 1+999 = 1000
    print()
    num1 = [1]
    l1 = populate_list(num1)
    output_list(l1)

    print('+')
    num2 = [9, 9, 9]
    l2 = populate_list(num2)
    output_list(l2)

    print('=')
    output_list(test.addTwoNumbers(l1, l2))

    # Test 2: 123+99889 =100012
    print()
    num1 = [1, 2, 3]
    l1 = populate_list(num1)
    output_list(l1)

    print('+')
    num2 = [9, 9, 8, 8, 9]
    l2 = populate_list(num2)
    output_list(l2)

    print('=')
    output_list(test.addTwoNumbers(l1, l2))

    # Test 3: 99+999 = 1098
    print()
    num1 = [9, 9]
    l1 = populate_list(num1)
    output_list(l1)

    print('+')
    num2 = [9, 9, 9]
    l2 = populate_list(num2)
    output_list(l2)

    print('=')
    output_list(test.addTwoNumbers(l1, l2))

    # Test 4: 123+45 = 168
    print()
    num1 = [1, 2, 3]
    l1 = populate_list(num1)
    output_list(l1)

    print('+')
    num2 = [4, 5]
    l2 = populate_list(num2)
    output_list(l2)

    print('=')
    output_list(test.addTwoNumbers(l1, l2))

    # Test 5: 1000 + 1001 = 2001
    print()
    num1 = [1, 0, 0, 0]
    l1 = populate_list(num1)
    output_list(l1)

    print('+')
    num2 = [1, 0, 0, 1]
    l2 = populate_list(num2)
    output_list(l2)

    print('=')
    output_list(test.addTwoNumbers(l1, l2))

    # Test 6: 1+999 =1000
    print()
    num1 = [1]
    l1 = populate_list(num1)
    output_list(l1)

    print('+')
    num2 = [9, 9, 9]
    l2 = populate_list(num2)
    output_list(l2)

    print('=')
    output_list(test.addTwoNumbers(l2, l1))
