def is_pangram(str):
    str = str.lower()
    alphabets = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
         'n', 'o', 'p', 'q', 'r', 's',    't', 'u', 'v', 'w', 'x', 'y', 'z'}
    
    for char in str:
        alphabets.discard(char)

    return len(alphabets) == 0

str = "a$ *+bc45ve"
# str = "the quick Brown fox jumps over the lazy dog"

res = is_pangram(str)
print(res)
