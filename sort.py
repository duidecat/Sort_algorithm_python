def bubbleSort(arr):
    for i in range (len(arr)):
        for j in range (0, len(arr) -i -1):
            if arr[j] > arr[j+1]:
                tam = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tam

def selectionSort(arr):
    for i in range (len(arr)):
        min_index = i
        for j in range (i +1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        tam = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = tam

def insertionSort(arr):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1

        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key


if __name__ == "__main__":
    array = [5,3,10,-2,-3]
    insertionSort(array)
    print(array)