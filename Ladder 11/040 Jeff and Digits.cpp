#include<iostream>
using namespace std;


int main()
{
int n, i, a, x, five = 0, zero = 0;
cin >> n;


for (i = 0; i < n; i++) {
cin >> a;
if (a == 5)
five++;
else
zero++;
}



if (zero == 0)
cout << -1;
else {
if (five < 9)
cout << 0;
else {
x = (five / 9) * 9;
for (i = 0; i < x; i++) cout << 5;
for (i = 0; i < zero; i++) cout << 0;
}
}
return 0;
}

