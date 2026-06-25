class Solution:
    def singleNumber(self, arr):
        result = 0

        for i in arr:
            result = result ^ i

        return result


arr = [1, 1, 2, 2, 3, 4, 4]

obj = Solution()
print(obj.singleNumber(arr))