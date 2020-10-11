'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


def sliding_window_max(nums, k):
    # Your code here
    # plalnning
    # go through array, find max of cuyrrent array
    # array gets larger with each k+1
    # find max

    start = 0
    array_of_maxs = []
    original_k = k
    for i in range(len(nums)):
        window = nums[start:k:1]
        start += 1
        k += 1
        array_of_maxs.append(max(window))

    return(array_of_maxs[:-(original_k-1)])
    # print(window)
   # print(max(window))
    #start += 1
    #k += 1
   # window = nums[start:k:1]
    # print(window)
    # print(max(window))


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
