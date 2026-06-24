class Frequency:
    def count_frequency(self, arr, x):
        count = 0

        for num in arr:
            if num == x:
                count += 1

        return count


arr = [1, 2, 3, 2, 4, 2, 5]

obj = Frequency()
res = obj.count_frequency(arr, 2)

print(res)