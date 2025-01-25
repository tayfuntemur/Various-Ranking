import random
import time

def generate_list(size):
    return [random.randint(1, 10000) for _ in range(size)] #1 ile 10000 arasında rasgele sayi oluştur.size kadar

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

def test_sorting_algorithms(sizes):
    algorithms = [
        ("Bubble Sort", bubble_sort),
        ("Selection Sort", selection_sort), 
        ("Insertion Sort", insertion_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort),
        ("Python's Sorted", sorted)
    ]
    
    for size in sizes:
        print(f"\nTesting with {size} elements:")
        original_list = generate_list(size)
        
        for name, algo in algorithms:
            test_list = original_list.copy()
            
            start_time = time.time()
            algo(test_list)
            end_time = time.time()
            
            print(f"{name}: {(end_time - start_time)*1000:.2f} ms")

# Test sorting algorithms
test_sorting_algorithms([1000, 5000, 10000])