'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # Your code here

    # n = len(arr)

    # if(n == 0):
    #     print (0)
    #     return 
    # # if n <= 1:
    # #     arr[n] = arr[n]
    # #     return arr
    
    # prod = 1 
    # for i in arr:
    #     prod *= i 

    # for i in arr: 
    #     val = int(prod*(i**-1))
    #     arr.append(val)
    # return arr 

    # Base case not passing on either for 2 elements 
    n = len(arr)
    if(n == 1): 
        print(0) 
        return
    
    left = [0]*n  
    right = [0]*n  
  
    prod = [0]*n  
 
    left[0] = 1
 
    right[n - 1] = 1
 
    for i in range(1, n):  
        left[i] = arr[i - 1] * left[i - 1]  
  
   
    for j in range(n-2, -1, -1):  
        right[j] = arr[j + 1] * right[j + 1]  
   
    for i in range(n):  
        prod[i] = left[i] * right[i]  
        arr.append(prod[i])
    
 
    # for i in range(n):  
    #     modified_arr = []
    #     mid = n // 2 
    #     arr[i] = modified_arr[mid - 1]

     
    mid = len(arr) // 2 
      
    return arr[mid:]

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
