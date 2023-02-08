def is_perfect(num):
    sum = 0
    for divisor in range(1, num):
        if num % divisor == 0:
            sum += divisor
    if sum == num:
        return "We have a perfect number!"
    return "It's not so perfect."


number = int(input())
print(is_perfect(number))

