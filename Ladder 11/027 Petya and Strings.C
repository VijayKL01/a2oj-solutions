#include <stdio.h>
#include <string.h>

int main() {
    char a[100], b[100];

    scanf("%s %s", a, b);

    int result = strcmp(a, b);

    if (result == 0) {
        printf("0\n");
    } else if (result > 0) {
        printf("1\n");
    } else {
        printf("-1\n");
    }

    return 0;
}
