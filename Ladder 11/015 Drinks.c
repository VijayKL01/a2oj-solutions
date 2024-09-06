#include <stdio.h>

int main() {
    int a;
    scanf("%d", &a);

    int c;
    double b = 0;
    for (int i = 1; i <= a; i++) {
        scanf("%d", &c);
        b += c;
    }

    double d = a;
    double e = b;

    printf("%.2f\n", b / d);
    return 0;
}
