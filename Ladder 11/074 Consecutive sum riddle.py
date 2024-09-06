a=int(input())
while(a!=0):
    n=int(input())
    if(n%2==0):
        print(-(n-1),'',n)
    else:
        print(n//2,'',n//2+1)
    a-=1
