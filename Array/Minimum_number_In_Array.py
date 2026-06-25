class Solution:
    def minimum(self, arr):
        mini = arr[0]

        for i in arr:
            if i < mini:
                mini = i

        return mini


arr = [5, 2, 8, 1, 9, 3]

obj = Solution()
print(obj.minimum(arr))