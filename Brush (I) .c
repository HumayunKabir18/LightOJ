#include <stdio.h>
int main() {
    int t,a,b,c,i,j;
    scanf("%d",&t);
    for (i=1;i<=t;i++)
    {
        c=0;
        scanf("%d",&a);
        for(j=1;j<=a;j++)
        {
            scanf("%d",&b);
            if (b>=0){
            c=c+b;
            }
        }
    printf("Case %d: %d\n",i,c);
    }
return 0;
}
