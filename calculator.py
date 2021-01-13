def number():
    n1 = float(input('Enter the first num : '))
    pr = input('Enter pram : ')
    n2 = float(input('Enter the sec num : '))
    pr = input('Enter pram : ')
    if pr == '=':
        return n1 + n2
    elif pr == '+':
        return number()
    else:
        return 'err'

# n1 = float(input('Enter the first num : '))
# n2 = float(input('Enter the sec num : '))

print(number())


