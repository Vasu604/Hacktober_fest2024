def quick_sort(arr):
    # Base case: An empty or single element array is already sorted
    if len(arr) <= 1:
        return arr

    # Choose a pivot (here we are choosing the last element as pivot)
    pivot = arr[-1]

    # Partition the array into three parts:
    # 1. Elements smaller than the pivot
    # 2. Elements equal to the pivot
    # 3. Elements greater than the pivot
    left = [x for x in arr[:-1] if x < pivot]
    equal = [x for x in arr if x == pivot]
    right = [x for x in arr[:-1] if x > pivot]

    # Recursively apply quicksort to the left and right parts, then combine
    return quick_sort(left) + equal + quick_sort(right)

# Example usage:
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)
