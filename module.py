def isEven(num):
    return num % 2 == 0


def isOdd(num):
    return not num % 2 == 0

nums = [4,5,6,7,8,9]

print(list(filter(isEven, nums)))
