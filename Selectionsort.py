# python program for Selection sort
def SelectionSort(arr, arr_size):
    # loop upto n-1
    for i in range(arr_size-1):
        min = i
        for j in range(i+1, arr_size):
            if(arr[j] < arr[min]):
                min = j
        # swapping the minimum index with i th index
        arr[i], arr[min] = arr[min], arr[i]


lst = list(map(int, input("Enter n numbers to be sort : ").split()))
SelectionSort(lst, len(lst))
print(lst)

# TIME COMPLEXITY A=O(n2) B=O(n2) W=O(n2)
# SPACE COMPLEXITY= O(1)
