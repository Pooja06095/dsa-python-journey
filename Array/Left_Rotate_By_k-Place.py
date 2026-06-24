class Left_rotate:
    def Left_Rotate(self, arr, d):
        
        d = d % len(arr)
        for i in range(d):
            first= arr[0]
            for num in range(len(arr)-1):
                arr[num]=arr[num+1]
            arr[len(arr)-1]= first
        return arr
    
arr = [1, 2, 3, 4, 5, 6, 7]
object = Left_rotate()
result = object.Left_Rotate(arr, 3)
print(arr)