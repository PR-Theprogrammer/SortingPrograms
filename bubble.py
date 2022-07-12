# program for BUBBLE sort
# Logic: Traverse array and check order such that arr[i]<arr[i+1] if it is not acc.to this condition then
# swap them ,continue this till it gets sorted
# so,Repeatedly swapping 2 adjacent elements if they are in wrong order

def Bubble(arr):
    n = len(arr)
    for i in range(len(arr)):
        for j in range(n-i-1):
            if(arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]


lst = list(map(int, input("Enter n numbers to be sort by Bubble sort: ").split()))
print(lst)
Bubble(lst)
print("Sorted Now:")
print(lst)
