try:
    t=int(input())
    for i in range(t):
        m,l=map(int,input().split())
        if m==l:
            print(f'Case {i+1}: {(m*4)+19}')
        else:
           f=abs(m-l)
           print(f'Case {i+1}: {((f+m)*4)+19}')
except:
    pass
