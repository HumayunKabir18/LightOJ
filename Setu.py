try:
    t=int(input())
    for i in range(t):
        z=int(input())
        c=0
        print(f'Case {i+1}:')
        for k in range(z):
            a=input()
            if a=='report':
                print(c)
            else:
                x=a.split(' ')
                x=int(x[1])
                c=c+x
except:
    pass
