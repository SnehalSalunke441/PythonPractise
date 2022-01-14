# Lecture 70, 71

def bubblesort(nums):
    n = len(nums) - 1
    for i in range(n):
        for j in range(n - i):
            if nums[j] > nums[j+1]:
                t = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = t

def insertsort(nums):
    n = len(nums) 
    for i in range(n):
        minp = i
        for j in range(i, n):
            if nums[j] < nums[minp]:
                minp = j
        t = nums[i]
        nums[i] = nums[minp]
        nums[minp] = t




nums = [5, 7, 3, 14, 2, 9, 8, 6]
#bubblesort(nums)
insertsort(nums)
print(nums)