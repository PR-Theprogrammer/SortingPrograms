# program for Insertion Sort
# LOGIC: Start traversing  from 1st index ,insert the i th element such that elements upto i th indesx remains sorted
def InsertionSort(arr, size):
    # starting from 1st index upto size of array
    for i in range(1, size):
        # key is the ith element
        key = arr[i]

        # initially declaring j=i-1 to compare i with earlier left hand side elements
        j = i-1
        while(key < arr[j] and j >= 0):
            arr[j+1] = arr[j]
            j -= 1

        # placing the ith key element after the element just smallar than it
        arr[j+1] = key


lst = list(map(int, input("Enter n numbers to be sort : ").split()))
InsertionSort(lst, len(lst))
print(lst)
