class Solution:
    def intersection(self, arr1, arr2):
        i = 0
        j = 0
        res = []

        while i < len(arr1) and j < len(arr2):

            if arr1[i] < arr2[j]:
                i += 1

            elif arr1[i] > arr2[j]:
                j += 1

            else:
                res.append(arr1[i])
                i += 1
                j += 1

        return res


arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 3, 5, 6]

obj = Solution()
print(obj.intersection(arr1, arr2))