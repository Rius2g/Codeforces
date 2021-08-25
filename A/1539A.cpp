#include <iostream>
using namespace std;

int main()
{
    int k;
    cin >> k;
    while(k--)
    {
        int n, x, t, sum, tid;
        cin >> n >> x >> t;
        long long mid = t/x;
        if(n < mid)
        {
            cout << n*(n-1)/2 << endl;
            continue;
        }
        long long lft =(n-mid);
        long long right = (mid-1)*mid/2;
        cout << lft+right << endl;

    }
}