def quicksort(array):
 if len(array) <=1:
  return array
 else:
  pivot  = array[(len(array)//2)]
 
  left = []
  right = []

  for i in range(len(array)):
   if array[i] > pivot:
    right.append(array[i])
   if array[i] < pivot:
    left.append(array[i])

  left = quicksort(left)
  right = quicksort(right)

  return left + [pivot] + right

arr = [3, 6, 2, 8, 1, 0, 4, 7, 9, 5]
print(quicksort(arr))





