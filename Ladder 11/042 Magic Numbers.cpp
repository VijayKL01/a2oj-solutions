#include <iostream>
#include <string>

using namespace std;

int main() {
    string input;
    cin >> input;

    bool contains_144 = false;
    for (int i = 0; i < input.length(); i++) {
        if (input[i] != '1' && input[i] != '4') {
            contains_144 = false;
            break;
        }

        if (i + 2 < input.length() && input[i] == '1' && input[i + 1] == '4' && input[i + 2] == '4') {
            contains_144 = true;
            i += 2;
        } else if (i + 1 < input.length() && input[i] == '1' && input[i + 1] == '4') {
            i++;
        }
    }

    if (contains_144) {
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }

    return 0;
}
