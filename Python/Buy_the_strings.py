#Problem from codeforces https://codeforces.com/contest/1440/problem/A

#Buy the String

T=int(input())
while T!=0:
    n,c0,c1,h=[int(i) for i in input().split()]
    v=list(input())
    ones,zeros=0,0
    #print(v)
    for i in v:
        if i=='0':
            zeros+=1
        elif i=='1':
            ones+=1
    total=0
    #('ones',ones)
    #print('zeros',zeros)
    if c0+h<=c1:
        total=c0*n+ones*h
        #print('if')
    elif c1+h<=c0:
        total=c1*n + zeros*h
        #print('elif')
    #elif c1==c0 and c0==h:
        #total=c1*ones+c0*zeros
    else:
        total=c1*ones+c0*zeros
        #print('else')
    
    print(total)
    T-=1
    
    