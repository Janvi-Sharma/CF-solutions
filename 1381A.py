#solve function takes care of individual test case
from collections import Counter
def solve():
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=Counter(a);d=Counter(b);flag=1
    for i in range(1,1001):
        if c[i]>0 and d[i]>0:
            print("YES")
            print(1,i)
            flag=0
            break
    if flag:
        print("NO")
for _ in range(int(input())):
    solve()
    
