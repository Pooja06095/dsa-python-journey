class Sort:
    def sort(self):
        zero_count = 0
        one_count = 0
        two_count = 0
        for i in arr:
            if i == 0:
                zero_count += 1
            elif i == 1:
                one_count += 1
            else:
                two_count += 1
        give =[0]* zero_count + [1]* one_count + [2]* two_count
        return give
arr = [0, 1, 2, 0, 1, 2, 1, 0]
obj = Sort()
res = obj.sort()
print(res)