nums = [3,2,4]
target = 6
for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i+1] + nums[j] == target:
            print([i,j])
            


