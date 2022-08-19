try:
    t=int(input())
    for i in range(t):
        a=list(map(int,input().split()))
        a.sort()
        if pow(a[2],2)== pow(a[0],2) + pow(a[1],2):
            print(f'Case {i+1}: yes')
        else:
            print(f'Case {i+1}: no')
except:
    pass
