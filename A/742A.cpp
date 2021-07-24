#include <iostream>
#include <math.h>
using namespace std;

int main()
{
    int a;
    while(cin>>a)
    {
        if(!a) cout <<1<<endl;
        else
        {
            int ans = a%4;
            if(ans == 0)
                cout << 6 << endl;
            if(ans == 1)
                cout << 8 << endl;
            if(ans == 2)
                cout << 4 << endl;
            if(ans == 3)
                cout << 2 << endl;
        }
    }
}