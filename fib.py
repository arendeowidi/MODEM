def fib(limit): #calculate fibonacci
    results=[]
    last=1
    slast=0
    while last < limit:
        results.append(last)
        new = last+slast
        slast=last
        last=new
    return results

print(fib(10))
