class Linear_Search:
    def linear_search(self, arr, x):
        for i in range(len(arr)):
            if arr[i] == x:
                return i
        return -1


arr = [10, 20, 30, 40, 50]

obj = Linear_Search()
res = obj.linear_search(arr, 30)

print(res)