#include <stdio.h>
#include <string.h>

int main() {
    char str[100], str2[100];
    scanf("%s %s", str, str2);

    int len1 = strlen(str);
    int len2 = strlen(str2);

    if (len1 != len2) {
        printf("NO\n");
        return 0;
    }

    int i;
    for (i = 0; i < len1 / 2; i++) {
        char temp = str[i];
        str[i] = str[len1 - i - 1];
        str[len1 - i - 1] = temp;
    }

    if (strcmp(str, str2) == 0) {
        printf("YES\n");
    } else {
        printf("NO\n");
    }

    return 0;
}
