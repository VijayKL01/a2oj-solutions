#include <bits/stdc++.h>
using namespace std;

int main()
{
    int num, a, b, c, r;
    cin >> num >> a >> b;

    c = num - a - 1;

    if (c > b)
    {
        r = b + 1;
    }
    else
    {
        r = c + 1;
    }

    cout << r;

    return 0;
}
