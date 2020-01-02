"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        144ms
        直接使用链表进行计算
        :param l1:
        :param l2:
        :return:
        """
        sum = 0
        carry = 0
        weishu = 1
        while l1 or l2:
            if l1 == None:
                sum = sum + (l2.val + carry)%10 * weishu
                carry = (l2.val + carry)//10
                l2 = l2.next
            elif l2 == None:
                sum = sum + (l1.val + carry)%10 * weishu
                carry = (l1.val + carry) // 10
                l1 = l1.next
            else:
                sum = sum + ((l1.val + l2.val + carry )%10) * weishu
                carry = (l1.val + l2.val + carry)//10
                l1 = l1.next
                l2 = l2.next
            weishu *=10
        if carry !=0:
            sum = sum + carry*weishu
        return self.list2link(sum)

    # def addTwoNumbers(self, l1, l2):
    #     """
    #     64 ms
    #     将链表转换成数字然后进行计算，最终再转换成链表
    #     :param l1:
    #     :param l2:
    #     :return:
    #     """
    #     x1 = self.link2num(l1)
    #     x2 = self.link2num(l2)
    #     print(x1)
    #     sum = x1+x2
    #     return self.list2link(sum)

    def addTwoNumbers(self,l1,l2):
        """
        64 ms
        :param l1:
        :param l2:
        :return:
        """
        a,b = l1,l2
        pre = ListNode(0)
        r = pre
        carry = 0
        while a or b:
            x = a.val if a else 0
            y = b.val if b else 0
            s = x + y + carry
            carry = s//10
            r.next = ListNode(s%10)
            r = r.next
            if a:
                a =a.next
            if b:
                b = b.next
        if carry>0:
            r.next = ListNode(carry)

        return pre.next


    def link2num(self,l):
        x = 0
        w =1
        while l:
            x = x+ l.val*w
            l = l.next
            w*=10
        return x

    def list2link(self,x):
        l = ListNode(None)
        if x<10:
            l.val = x
            return l
        l.val = x%10
        # print(l.val)
        x = x//10
        l1= l
        while x:
            now = ListNode(None)
            now .val= x%10
            # print(now.val)
            x = x//10
            l1.next = now
            l1 = l1.next
        return l

def main():
    s = Solution()
    l = s.list2link(342)
    l2 = s.list2link(465)

    a = s.addTwoNumbers(l, l2)
    while a:
        print(a.val)
        a = a.next

if __name__ == '__main__':
    main()