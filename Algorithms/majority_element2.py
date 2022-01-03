# Uses python3
import sys

def get_majority_element(nums, left, right):
    count = 1
    major = nums[left]
    for i in range(left +1,right):
        if count == 0:
            count = 1
            major = nums[i]
        elif nums[i] == major:
            count += 1
        else:
            count -= 1    
    return major
    
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)

        