# QUICK SORT PROGRAM
# pivot element= last element of array
def quickSort(arr, low, high):
    if(low < high):
        # First find the pivot element index by calling partition()
        pivot_index = partition(arr, low, high)
        # sorting left hand side of pivot element
        quickSort(arr, low, pivot_index-1)

        # sorting right hand side of pivot element
        quickSort(arr, pivot_index+1, high)


def partition(arr, low, high):
    # set last element as pivot
    pivot = arr[high]
    i = low-1

    # check for correct position of pivot element
    for j in range(low, high):
        if(arr[j] < pivot):
            i += 1
        # swapping
            arr[i], arr[j] = arr[j], arr[i]
    i += 1
    # final swap pivot element with max element specified by i
    arr[i], arr[high] = arr[high], arr[i]
    return i


arr = [56, 2, 7, 3, 4, 0, 99]
low = 0
high = len(arr)-1
quickSort(arr, low, high)
print("After Quick sort:")
print(arr)
