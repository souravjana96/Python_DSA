def fib(n):
    if n == 0 or n == 1:
        return n
    
    curr_num = fib(n-1) + fib(n-2)
    return curr_num
        
    


n = 2
res_num = fib(n)
print(n, "'th fibonacci number is: ", res_num)