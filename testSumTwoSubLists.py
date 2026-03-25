def find_even_index(arr):

    for index in range(0, len(arr)):

        leftList = arr[:index]
        rightList = arr[index+1:]
        leftSum = sum(leftList)
        rightSum = sum(rightList)

        if (leftSum == rightSum):
            return index

    return -1

arr = [1,100,50,-51,1,1]
print(find_even_index(arr))
