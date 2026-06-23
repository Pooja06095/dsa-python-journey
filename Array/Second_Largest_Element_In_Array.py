arr = [12, 35, 1, 10, 34, 1]
largest = -1
second_largest = -1
for num in arr:
    if num > largest:
        second_largest = largest
        largest = num

    elif num > second_largest and num != largest:
        second_largest = num
print("Second Largest", second_largest)


