#include <stdio.h>
#include <string.h>

int main() {
    char s[100];
    scanf("%s", s);

    int i, cnt = 0;

    for (i = 0; i < strlen(s); i++) {
        if (!(s[i] == 'W' && s[i + 1] == 'U' && s[i + 2] == 'B')) {
            printf("%c", s[i]);
            cnt++;
        } else {
            i += 2;
            if (cnt > 0) {
                printf(" ");
            }
            cnt = 0;
        }
    }

    return 0;
}
