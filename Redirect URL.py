try:
    t=int(input())
    for c in range(t):
        x=input()
        x=list(x)
        if x[4]=='s':
            k=''.join(x)
            print(f'Case {c+1}: {k}')
        else:
            x.insert(4,'s')
            k=''.join(x)
            print(f'Case {c+1}: {k}')
except:
    pass
