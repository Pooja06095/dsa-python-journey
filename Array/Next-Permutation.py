class NextPermutation:
    def next_permutation(self):
        n = len(arr)

        # Step 1: Pivot find karo
        pivot = -1
        for i in range(n - 2, -1, -1):
            if arr[i] < arr[i + 1]:
                pivot = i
                break

        # Agar pivot nahi mila to array descending order me hai
        if pivot == -1:
            arr.reverse()
            return arr

        # Step 2: Pivot se bada sabse chhota element dhoondo
        for i in range(n - 1, pivot, -1):
            if arr[i] > arr[pivot]:
                arr[i], arr[pivot] = arr[pivot], arr[i]
                break

        # Step 3: Pivot ke baad wale part ko reverse karo
        arr[pivot + 1:] = reversed(arr[pivot + 1:])

        return arr


arr = [1, 2, 3]

obj = NextPermutation()
res = obj.next_permutation()

print(res)