class Leaders:
    def leader(self):
        max_right = arr[-1]
        leaders = [max_right]
        for i in reversed(arr[:-1]):
            if i> max_right:
                max_right = i
                leaders.append(i)
        leaders.reverse()
        return leaders
arr = [16, 17, 4, 3, 5, 2]
obj = Leaders()
res = obj.leader()
print(res)
            
