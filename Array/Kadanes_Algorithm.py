class MaximumSubarray:
    def max_sum(self):
        current_sum = 0
        max_sum = arr[0]

        for i in arr:
            current_sum += i

            max_sum = max(max_sum, current_sum)
            if current_sum < 0:
                current_sum = 0

        return max_sum
    
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
obj = MaximumSubarray()
res = obj.max_sum()
print(res)