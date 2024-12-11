# san so nguyen to tu 1 mang  0 - n => output: mang gom cac so nguyen to
def selectionSort_min(arr):
    for i in range(len(arr)):
        min_index = i 
        
        for j in range (i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
                
        tam = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = tam 
        
    return arr
    
def selectionSort_max(arr):
    for i in range(len(arr)):
        max_index = i
        
        for j in range (i + 1, len(arr)):
            if arr[j] < arr[max_index]:
                max_index = j
                
        tam = arr[max_index]
        arr[max_index] = arr[i]
        arr[i] = tam 
        
    return arr

if __name__ == "__main__":
    arr = [0, 2, 4, 6, 9, 1, 3, 5, 8, 7]
    print(selectionSort_max(arr)) 
    
    