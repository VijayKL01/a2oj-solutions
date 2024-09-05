#include <iostream>
using namespace std;

int main()
{
    int num, a, b, c;
    int sum_a = 0, sum_b = 0, sum_c = 0;
    cin >> num;

    while (num--)
    {
        cin >> a >> b >> c;
        sum_a += a;
        sum_b += b;
        sum_c += c;
    }

    if (sum_a == 0 && sum_b == 0 && sum_c == 0)
        cout << "YES";
    else
        cout << "NO";
}
