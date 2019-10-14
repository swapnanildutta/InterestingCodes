# Python3 code to linearly search x in arr[].  
# If x is present then return its location, otherwise return 0
  
def search(arr, x):
    for i in arr: 
        if (i == x): 
            return arr.index(i) 
    return 0 
  
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
result = search(arr, x) 
if(result == 0): 
    print("Element is not present in array") 
else: 
    print("Element is present at index", result)
