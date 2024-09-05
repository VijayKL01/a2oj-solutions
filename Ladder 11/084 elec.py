t=int(input())
while(t!=0):
    lst=input().split(' ')
    for i in range(len(lst)):
        lst[i]=int(lst[i])
        
    x=max(lst)
    maxx=0
    if(x==lst[0]):
        maxx+=1
    if(x==lst[1]):
        maxx+=1
    if(x==lst[2]):
        maxx+=1
    if(maxx==3):
        print('1','1','1')
        print('\n')
    elif(maxx==2):
        for i in range(len(lst)):
            if(lst[i]==x):
                print('1',end=' ')
            else:
                print(x-(lst[i]-1),end=' ')
        print('\n')
    else:
        
        for i in range(len(lst)):
            if(lst[i]==x):
                print('0',end=' ')
            else:
                print(x-(lst[i]-1),end=' ')
        print('\n')
    t-=1
