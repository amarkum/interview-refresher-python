"""
Bubble Sort Algorithm
"""


def sort(nums):
    for i in range(len(nums) - 1, 0, -1):
        for j in range(0, i):
            if nums[j] > nums[j + 1]:
                temp = nums[j + 1]
                nums[j + 1] = nums[j]
                nums[j] = temp
    return nums


if __name__ == '__main__':
    numbers = [1, 9, 10, 3, 9, 5, 4, 5, 6]
    print(sort(numbers))
