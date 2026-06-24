class Right_rotate:
    def right_rotate(self, arr, d):
        d = d % len(arr)
        for i in range(d):
            first = arr[-1]
            for num in range(len(arr)-1,0,-1):
                arr[num]= arr[num -1]
            arr[0]= first
        return arr
arr = [1,2,3,4,5,6,7]
obj = Right_rotate()
res = obj.right_rotate(arr, 3)
print(res)