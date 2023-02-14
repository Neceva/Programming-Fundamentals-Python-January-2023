def found_palindrome(word):
    if word == word[::-1]:
        return word


words = input().split()
palindrome = input()
palindrome_list = [word for word in words if found_palindrome(word)]
counter_palindrome = palindrome_list.count(palindrome)

print(palindrome_list)
print(f"Found palindrome {counter_palindrome} times")