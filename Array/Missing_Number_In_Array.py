class Missing_number:
    def missing_number(self):
        n = len(arr) + 1
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(arr)

        missing = expected_sum - actual_sum

        return missing


arr = [1, 2, 4, 5]

obj = Missing_number()
result = obj.missing_number()

print(result)