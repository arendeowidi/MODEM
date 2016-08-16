def MissingNumber(a, b):
    a = set(a)
    b = set(b)
    if len(a) == len(b):
        return 0
    elif len(a)==0 and len(b)==0:
        return 0
    elif len(a) > len(b) or len(b) > len(a):
        if len(a) > len(b):
            z = list(a-b)
            return z[0]
        else:
            z = list(b-a)
            return z[0]

a = [1, 4]
b = [3, 6]
print MissingNumber(a, b)
