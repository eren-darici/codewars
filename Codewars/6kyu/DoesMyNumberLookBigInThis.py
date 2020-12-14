def narcissistic(value):
    l = len(str(value))
    sum = 0
    

    for digit in str(value):
        sum+= int(digit) ** l

    if value == sum:
        return True
    else:
        return False
