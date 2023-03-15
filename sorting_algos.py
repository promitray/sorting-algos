import timeit
import random
import matplotlib.pyplot as plt

def bubble_sort(unsorted_array):
    sorted = False
    while sorted == False:
        sorted = True
        for i in range(len(unsorted_array) -1):
          if unsorted_array[i + 1] < unsorted_array[i]:
                sorted = False
                unsorted_array[i], unsorted_array[i + 1] = unsorted_array[i + 1], unsorted_array[i] 
                
    return unsorted_array

def selection_sort(unsorted_array):
    for i in range(0, len(unsorted_array) - 1):
        min_index = i
        for j in range(i + 1, len(unsorted_array)):
            if unsorted_array[j] < unsorted_array[i]:
                min_index = j
        unsorted_array[i], unsorted_array[min_index] = unsorted_array[min_index], unsorted_array[i]
    return unsorted_array

def insertion_sort(unsorted_array):
    for i in range(1, len(unsorted_array)):
     for j in range(i,1, -1):
         #print (i, j, unsorted_array[j], unsorted_array[j-1] )
         if unsorted_array[j] < unsorted_array[j-1]:
             unsorted_array[j], unsorted_array[j-1] = unsorted_array[j-1], unsorted_array[j]
      
    return unsorted_array

def get_min(unsorted_array):
    min_element = unsorted_array[0]
    for element in unsorted_array[0:]:
      if element < min_element:
          min_element = element
    return min_element

def sort_array(array_1, array_2):
    sorted_array, i, j = [], 0, 0
    
    while i <  len(array_1) and j < len(array_2):
     if array_1[i] < array_2[j]:
        sorted_array.append(array_1[i])
        i += 1
     else:
        sorted_array.append(array_2[j])
        j += 1

    sorted_array += array_1[i:len(array_1)]
    sorted_array += array_2[j:len(array_2)]

    return sorted_array

def merge_sort(arr):
   if len(arr) <=1:
      return arr
   
   mid = len(arr)//2
   left = arr[:mid]
   right = arr[mid:]

   left = merge_sort(left)
   right = merge_sort(right)
 

   return (sort_array(left, right))

def quicksort(array):
 if len(array) <=1:
  return array
 else:
  pivot  = array[(len(array)//2)]
 
  left = []
  right = []
  equal = []

  for i in range(len(array)):
   if array[i] > pivot:
    right.append(array[i])
   if array[i] < pivot:
    left.append(array[i])
   if array[i] == pivot:
    equal.append(array[i])

  left = quicksort(left)
  right = quicksort(right)

  return left + equal + right

print (selection_sort([2, 2, 8, 3, 2, 5, 2, 3, 7, 2, 9]))
print (bubble_sort([2, 2, 8, 3, 2, 5, 2, 3, 7, 2, 9]))
print (insertion_sort([2, 2, 8, 3, 2, 5, 2, 3, 7, 2, 9]))
print (merge_sort([2, 2, 8, 3, 2, 5, 2, 3, 7, 2, 9]))
print (quicksort([2, 2, 8, 3, 2, 5, 2, 3, 7, 2, 9]))


sorting_functions = {
    'bubble_sort': bubble_sort,
    'selection_sort': selection_sort,
    'merge_sort': merge_sort,
    'quicksort': quicksort
}

# Generate arrays of different sizes and run sorting algorithms on them
array_sizes = [10, 100, 1000, 10000]  # Modify this list to include other sizes
results = {}
for size in array_sizes:
    arr = [random.randint(0, size) for _ in range(size)]
    result = {}
    for name, func in sorting_functions.items():
        stmt = f"{name}({arr})"
        setup = f"from __main__ import {name}"
        runtime = timeit.timeit(stmt, setup=setup, number=10)
        result[name] = runtime
    results[size] = result

# Plot the results
for name in sorting_functions.keys():
    plt.plot(array_sizes, [results[size][name] for size in array_sizes], label=name)
plt.legend()
plt.xlabel('Array Size')
plt.ylabel('Runtime (seconds)')
plt.show()
