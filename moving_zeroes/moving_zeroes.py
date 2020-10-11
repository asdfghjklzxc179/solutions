'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    # Your code here
    # input is an array
    # output is (?) the first element in the altered array (altered array is zeros moved to the right, or non zeros to the left of the zeros)
    zeros = []
    # go through array, slice the zero, append the sliced zero
    for element in arr:
        if element == 0:
            arr.remove(element)
            zeros.append(element)
            print(zeros)

    for i in zeros:
        arr.append(i)

    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
