def narcissistic(value):
    return value == sum([int(digit) ** len(str(value)) for digit in str(value)])