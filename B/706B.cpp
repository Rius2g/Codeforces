#include <iostream>
#include<stdio.h>
#include<string.h>
#include<cmath>
#include<algorithm>
using namespace std;

int main()
{
    int a1[100005],a2[100005];
    int n=0,m=0;

    while(scanf("%d",&n)!=EOF)
    {
        for(int i = 0; i<n; i++)
        {
            scanf("%d", &a1[i]);
        }
        scanf("%d", &m);
        sort(a1,a1+n);
        for(int i=0; i < m; i++)
        {
            scanf("%d", &a2[i]);

            int q =upper_bound(a1,a1+n,a2[i]) -a1;
            printf("%d\n", q);
        }
    }
}