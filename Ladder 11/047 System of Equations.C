#include <stdio.h>
#include <string.h>

int main() {
    char a[100];
    scanf("%s", a);
    int b = strlen(a);
    int c = 0;

    for (int i = 0; i < b; i++) {
        if (a[i] == '1' && a[i + 1] == '4' && a[i + 2] == '4') {
            i += 2;
        } else if (a[i] == '1' && a[i + 1] == '4') {
            i++;
        } else if (a[i] != '1' && a[i] != '4') {
            c = 1;
            break;
        }
    }

    if (c == 0) {
        printf("YES\n");
    } else {
        printf("NO\n");
    }

    return 0;
}
