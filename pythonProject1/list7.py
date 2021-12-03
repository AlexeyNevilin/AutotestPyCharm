a=[int(i) for i in input().split()]
n=len(a)
if n==1:
    print(a[0])
else:
    for i in range(n-1):
        print(a[i-1]+a[i+1], end=" ")
    print(a[n-2]+a[0])