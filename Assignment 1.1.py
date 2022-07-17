n1 = 0
n2 = 1
n = 1
print(n1,n2, end=" ")
while n < 34:
    n1 = n2
    n2 = n
    n = n1+n2
    print(n, end=" ")