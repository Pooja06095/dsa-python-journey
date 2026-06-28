class LongestConsecutive:
    def longest_consecutive(self):
        arr.sort()

        count = 1
        max_count = 1

        for i in range(1, len(arr)):

            # Duplicate element ko ignore karo
            if arr[i] == arr[i - 1]:
                continue

            # Consecutive hai
            elif arr[i] == arr[i - 1] + 1:
                count += 1

            # Sequence toot gayi
            else:
                count = 1

            max_count = max(max_count, count)

        return max_count


arr = [100, 4, 200, 1, 3, 2]

obj = LongestConsecutive()
res = obj.longest_consecutive()

print(res)