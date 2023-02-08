def palindrome_checker(list):
    for num in list:
        is_palindrome = num[0] == num[-1]
        print(is_palindrome)


positive_ints = input().split(", ")
palindrome_checker(positive_ints)
