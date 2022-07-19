# MERGE SORT PROGRAM
def mergeSort(arr):
    if len(arr) > 1:

        #  calculate the mid point
        mid = len(arr)//2
        L = arr[:mid]
        M = arr[mid:]

        # Sort the two subarray
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = M[j]
                j += 1
            k += 1

        # copy remaining elements of either 2 arrays into main array
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            arr[k] = M[j]
            j += 1
            k += 1


arr = [56, 2, 7, 3, 4, 0, 99, 33]
low = 0
high = len(arr)-1
print("Before Quick sort:")
print(arr)
mergeSort(arr)
print("After Quick sort:")
print(arr)
