#include <bits/stdc++.h>
using namespace std;

/*---------------------------------------------------------------------------------------------------------------------------*/

void solve()
{

    int n, num, sum(0);
    cin >> n;

    while (cin >> num)
        sum += num;

    cout << ((sum % n) ? n - 1 : n);
}

int main()
{
    int ts;
    ts = 1;
    

    for (int i = 1; i <= ts; i++)
    {
       
        solve();
    }

    return 0;
}
