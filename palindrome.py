print("Enter the string you want check for palindrome")
s = input()

def check(s):
    low = 0
    high = len(s)-1
    while low < high:
        if s[low] == s[high]:
            low += 1
            high -= 1

        else:
            print(f"This {s} is not a palindrome")
            break

    else:
        print(f"This {s} is a palindrome")

check(s)