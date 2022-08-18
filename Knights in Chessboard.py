try:
    t=int(input())
    for i in range(t):
        a,b=map(int,input().split())
        if a==1 or b==1:
            print(f'Case {i+1}: {int(a*b)}')
        elif a==2 or b==2:
            a=a*b
            c=int(a/8)*4
            d=int(a%8)
            if d<=4:
                c=c+d
            elif d>4:
                c=c+4
            print(f'Case {i+1}: {int(c)}')
        else:
            if (a*b)%2==0:
                print(f'Case {i+1}: {int((a*b)/2)}')
            else:
                print(f'Case {i+1}: {int((a*b)/2)+1}')
except:
    pass
        
