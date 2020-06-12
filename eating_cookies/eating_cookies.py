'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # Your code here
    if n < 0: 
        pass 
    elif n == 0: 
        return 1 
    if n == 1 or n == 2:
        return n 

    elif n == 3: 
        return 4
    else: 
        return eating_cookies(n-1) + eating_cookies(n - 2) + eating_cookies(n - 3)

# def eating_cookies(n, cache =None):
#     # Your code here
    
#     if cache == None: 
#         cache = [0] * (n + 1)
#     if n <= 1: 
#         cache[n] = 1
#     elif n == 2: 
#         cache[n] = 2 
#     elif cache[n] == 0: 
   
#         cache[n]= eating_cookies(n-1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)
    

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
