class MoveZeros:
    def move_ALL_zeros(self,arr):
        x = 0
        for num in arr:
            if num!=0:
                arr[x] =num
                x += 1
        while x < len(arr):
            arr[x]=0
            x += 1
        return arr
arr = [1,0,2,3,0,4,0,1]

obj = MoveZeros()

result = obj.move_ALL_zeros(arr)

print(result)            