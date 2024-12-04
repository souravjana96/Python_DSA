
def countWays(curr_step, n):
    if curr_step > n:
        return 0

    if curr_step == n:
        return 1

    return countWays(curr_step + 1, n) + countWays(curr_step + 2, n)



n = 3
print(countWays(0,n))