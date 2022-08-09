try:
    t=int(input())
    for i in range(t):
        x=int(input())
        if x>10:
            k=x-10
            print(f'10 {k}')
        elif x%2==0:
            print(f'{int(x/2)} {int(x/2)}')
        else:
            print(f'{x-1} {1}')
except:
    pass
