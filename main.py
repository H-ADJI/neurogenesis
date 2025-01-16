import sys


# Function to find the maximum product of two integers in a list
def findMaximumProduct(A):

    # to store the maximum and second maximum element in a list
    max1 = A[0]
    max2 = -sys.maxsize

    # to store the minimum and second minimum element in a list
    min1 = A[0]
    min2 = sys.maxsize

    for i in range(1, len(A)):

        # if the current element is more than the maximum element,
        # update the maximum and second maximum element
        if A[i] > max1:
            max2 = max1
            max1 = A[i]

        # if the current element is less than the maximum but greater than the
        # second maximum element, update the second maximum element
        elif A[i] > max2:
            max2 = A[i]

        # if the current element is less than the minimum element,
        # update the minimum and the second minimum
        if A[i] < min1:
            min2 = min1
            min1 = A[i]

        # if the current element is more than the minimum but less than the
        # second minimum element, update the second minimum element
        elif A[i] < min2:
            min2 = A[i]

        # otherwise, ignore the element

    # choose the maximum of the following:
    # 1. Product of the maximum and second maximum element or
    # 2. Product of the minimum and second minimum element
    if max1 * max2 > min1 * min2:
        print("Pair is", (max1, max2))
    else:
        print("Pair is", (min1, min2))


if __name__ == "__main__":

    A = [-1, 1]
    findMaximumProduct(A)
