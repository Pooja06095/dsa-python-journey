class Two_Sum:
    def two_sum(self):
        seen = set()
        for num in arr:
            complement = target - num

            if complement in seen:
                return True
            seen.add(num)
        return False
arr = [2, 7, 11, 15]
target = 9
obj = Two_Sum()
res = obj.two_sum()
print(res)