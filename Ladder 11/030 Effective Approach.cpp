#include <bits/stdc++.h>
using namespace std;

int main()
{
	int a, num, i, j;
	cin >> a;
	int arr1[a + 1], arr2[a];
	for (i = 0, j = a - 1; i < a; i++, j--) {
		cin >> num;
		arr1[num] = i;
		arr2[num] = j;
	}



	long long p1 = 0, p2 = 0;

	int m, num2;
	cin >> m;
	for (i = 0; i < m; i++) {
		cin >> num2;
		p1 += arr1[num2] + 1;
		p2 += arr2[num2] + 1;

	}

	printf("%I64d %I64d\n", p1, p2);
	return 0;
}
