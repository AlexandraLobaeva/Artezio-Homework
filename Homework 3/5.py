def f():
    u=input().split()
    n=[]
    for i in u:
        n.append(float(i))
    return min(n,key=abs)
print(f())
