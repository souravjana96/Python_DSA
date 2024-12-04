def generateSubsequences(arr, index, res):
    if index == len(arr):
        print(res)
        return
    
    generateSubsequences(arr, index+1, res)
    
    generateSubsequences(arr, index+1, res + [arr[index]])


arr = [1, 2, 3]
generateSubsequences(arr, 0, [])