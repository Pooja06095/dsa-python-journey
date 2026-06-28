class Rearrange_Array:
    def alternative(self):
        left = 0
        right = len(arr)-1
        result = []
        while left <= right: 
            result.append(arr[left])
            if left != right:
                result.append(arr[right])
            left += 1
            right -= 1
        return result
arr = [10, 20, 30, 40, 50]
obj = Rearrange_Array()
res = obj.alternative()
print(res)