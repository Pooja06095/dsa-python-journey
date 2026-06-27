class majority:
    def Majority_number(self):
        for i in arr:
            if arr.count(i) > len(arr)//2:
                return i
        return -1
arr = [1, 2, 3, 2, 4, 2, 5, 2, 2] 
obj = majority()
res = obj.Majority_number()   
print(res)  
           
        