try:
    t=int(input())
    for i in range(t):
        x1,y1,x2,y2=map(int,input().split())
        p=int(input())
        print(f'Case {i+1}:')
        for j in range(p):
            x,y=map(int,input().split())
            if x>x1 and x<x2 and y>y1 and y<y2:
                print('Yes')
            else:
                print('No')
except:
    pass
