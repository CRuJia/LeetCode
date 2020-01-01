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



    def hello(self, str= 'sad'):
        print(str)

def main():
    s = Solution()
    # nums = [2, 7, 11, 15]
    # target = 9
    nums = [3,3]
    target = 6
    r = s.twoSum(nums,target)
    print(r)

    print('asff')

if __name__ == '__main__':
    main()

