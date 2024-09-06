#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t, a, b, c, result=0;
    
    cin >> t;
    while(t--){
        cin >> a;
        cin >> b;
        cin >> c;
        
        if (a+b+c>=2) result++;
    }
    cout << result;

    return 0;
}
