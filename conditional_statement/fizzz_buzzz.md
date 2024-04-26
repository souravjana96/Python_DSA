### Description

You are given a number called 'n' (0 < n < 100).
For all numbers in range [1, n] -

Print 'FizzBuzz' if the number is divisible by 3 and 5 both.

Print 'Fizz' if the number is divisible by 3.

Print 'Buzz' if the number is divisible by 5.

Else print the number as it is.

### Sample Input

```
n = 3
```

### Sample Output

```
1
2
Fizz
```

## Solution

```
def fizz_buzz(num):
    for i in range(1, num + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# calling the function
fizz_buzz(15)

```
