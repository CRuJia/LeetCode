"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    # def twoSum(self, nums, targets):
    #     """
    #     暴力破解
    #     	5912 ms
    #     :param nums:
    #     :param targets:
    #     :return:
    #     """
    #     for i in range(len(nums)):
    #         for j in range(i+1,len(nums)):
    #             if nums[i]+nums[j] == targets:
    #                 return [i,j]
    #
    # def twoSum(self, nums, targets):
    #     """
    #     	1164 ms
    #     :param nums:
    #     :param targets:
    #     :return:
    #     """
    #     for i in range(len(nums)):
    #         if targets - nums[i] in nums and nums.index(targets - nums[i]) != i:
    #             return [i, nums.index(targets - nums[i])]

    # def twoSum(self, nums, targets):
    #     """
    #     816 ms
    #     :param nums:
    #     :param targets:
    #     :return:
    #     """
    #     for i in range(len(nums)-1):
    #         temp = nums[i+1:]
    #         if targets - nums[i] in temp :
    #             return [i, nums.index(targets - nums[i],i+1)]

    # def twoSum(self, nums, target):
    #     """
    #     	60 ms
    #     :param nums:
    #     :param target:
    #     :return:
    #     """
    #     hashmap = {}
    #     for ind, num in enumerate(nums):
    #         hashmap[num] = ind
    #
    #     for i, num in enumerate(nums):
    #         j = hashmap.get(target - num)
    #         if j is not None and i != j:
    #             return [i, j]

    def twoSum(self,nums, target):
        """
        48 ms
        :param nums:
        :param target:
        :return:
        """
        hashmap = {}
        for i,num in enumerate(nums):
            if hashmap.get(target-num) is not None:
                return [i,hashmap.get(target-num)]
            hashmap[num]=i




def main():
    s = Solution()
    # nums = [2, 7, 11, 15]
    # target = 9
    nums = [3,3]
    target = 6
    r = s.twoSum(nums,target)
    print(r)


if __name__ == '__main__':
    main()

