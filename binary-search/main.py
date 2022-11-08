
# This algorithm runs in logarithmic time

def binary_search(arr, num):
  low = 0
  high = len(arr) - 1
  while low <= high:
    mid = int((high + low) / 2)
    if(arr[mid] == num):
      return mid
    elif (arr[mid] > num):
      high = mid - 1
    else:
      low = mid + 1
  return None 

numList = [2, 4, 7, 9, 15, 35, 44, 56]

print(binary_search(numList, 13))
print(binary_search(numList, 35))
