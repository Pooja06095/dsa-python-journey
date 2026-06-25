class Solution:
    def findMaxConsecutiveOnes(self, nums):
        count = 0
        maxi = 0

        for i in nums:
            if i == 1:
                count += 1
                maxi = max(maxi, count)
            else:
                count = 0

        return maxi


nums = [1, 1, 0, 1, 1, 1]

obj = Solution()
print(obj.findMaxConsecutiveOnes(nums))