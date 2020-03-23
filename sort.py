# Implement bubbleSort, mergeSort, insertionSort, quickSort, selectionSort

# just to remember recursion
def fibonacci(number):
    if number < 2:
        return number
    return (fibonacci(number-1) + fibonacci(number-2))

def swap(arr, i1, i2):
    tmp = arr[i1]
    arr[i1] = arr[i2]
    arr[i2] = tmp
    return arr

def mergeSortedArrays(arr1, arr2):
    res = []
    resi = 0
    while len(arr1) > 0 and len(arr2) > 0:
        if(arr1[0] < arr2[0]):
            res.append(arr1[0])
            arr1.remove(arr1[0])
        else:
            res.append(arr2[0])
            arr2.remove(arr2[0])
        resi += 1
    res.extend(arr1)
    res.extend(arr2)
    return res

def bubbleSort(arr):
    sw = True
    while sw == True:
        sw = False
        for i in range(len(arr)-1):
            if(arr[i] > arr[i+1]):
                sw = True
                swap(arr, i, i+1)
    return arr

def mergeSort(arr):
    if len(arr) == 1:
        return arr
    if len(arr) == 2:
        if(arr[0] > arr[1]):
            swap(arr, 0, 1)
        return arr
        
    m = len(arr)/2
    resLeft = mergeSort(arr[:m])
    resRight = mergeSort(arr[m:])
    return mergeSortedArrays(resLeft,resRight)

# Could be nicer, I guess
def insertionSort(arr):
    for i in range(1,len(arr)):
        sw = True
        ii = i
        while sw == True and ii > 0:
            sw = False
            if arr[ii] < arr[ii-1]:
                swap(arr, ii, ii-1)
                sw = True
                ii -= 1
    return arr

# Choose last item as pivot
def quickSort(arr):
    if len(arr) == 2:
        if arr[0] > arr[1]:
            swap(arr,0,1)
        return arr
    if len(arr) == 1:
        return arr

    pivi = len(arr)-1
    i = 0
    while i < pivi-1:
        if arr[i] > arr[pivi]:
            while arr[pivi] < arr[pivi-1]:
                swap(arr,pivi,pivi-1)
                pivi -= 1
            swap(arr,i,pivi-1)
            swap(arr,pivi,pivi-1)
            pivi -= 1
        i += 1
    resLeft = quickSort(arr[:pivi])
    resRight = quickSort(arr[pivi:])
    return mergeSortedArrays(resLeft,resRight)

def selectionSort(arr):
    for k in range(len(arr)-1):
        sm = k
        for i in range(k+1,len(arr)):
            if arr[i] < arr[sm]:
                sm = i
        swap(arr,k,sm)
    return arr

arr = [6, 5, 3, 1, 8, 7, 2, 4]
arr = [6, 5, 3, 1, 4]
arr = [6, 5, 3, 1, 8, 7, 2, 4, 9]
#print(bubbleSort(arr))
#print(mergeSort(arr))
#print(insertionSort(arr))
#print(quickSort(arr))
print(selectionSort(arr))
