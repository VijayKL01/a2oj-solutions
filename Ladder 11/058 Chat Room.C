#include <stdio.h>
#include <string.h>

int main() {
    char a[100];
    scanf("%s", a);
    int b = strlen(a);
    int c = 0, d = 0, e = 0, f = 0, g = 0;

    for (int i = 0; i < b; i++) {
        if (a[i] == 'h') {
            c = i;
            break;
        }
    }
    for (int i = c + 1; i < b; i++) {
        if (a[i] == 'e') {
            d = i;
            break;
        }
    }
    for (int i = d + 1; i < b; i++) {
        if (a[i] == 'l') {
            e = i;
            break;
        }
    }
    for (int i = e + 1; i < b; i++) {
        if (a[i] == 'l') {
            f = i;
            break;
        }
    }
    for (int i = f + 1; i < b; i++) {
        if (a[i] == 'o') {
            g = i;
            break;
        }
    }

    if (0 <= c && c < d && d < e && e < f && f < g) {
        printf("YES\n");
    } else {
        printf("NO\n");
    }

    return 0;
}
