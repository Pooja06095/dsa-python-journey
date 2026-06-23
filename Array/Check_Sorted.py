arr = [1, 2, 3, 4, 5]
is_sorted = True

for i in range(len(arr)-1):
    if arr[1]> arr[i + 1]:
        is_sorted = False
        break
print(is_sorted)