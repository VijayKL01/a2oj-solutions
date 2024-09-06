#include <iostream>
#include <string>

using namespace std;

int main() {
    string a;
    cin >> a;
    int b = a.length();
    string d = "";

    for (int i = 0; i < b; i++) {
        a[i] = tolower(a[i]);
        if (!strchr("aeiouy", a[i])) {
            d += "." + a[i];
        }
    }

    cout << d << endl;

    return 0;
}
