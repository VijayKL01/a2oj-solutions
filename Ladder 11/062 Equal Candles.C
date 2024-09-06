#include <stdio.h>

int main() {
    int t;
    scanf("%d", &t);

    while (t--) {
        int n;
        scanf("%d", &n);

        int lst[n];
        for (int i = 0; i < n; i++) {
            scanf("%d", &lst[i]);
        }

        int x = lst[0];
        for (int i = 1; i < n; i++) {
            if (lst[i] < x) {
                x = lst[i];
            }
        }

        int s = 0;
        for (int i = 0; i < n; i++) {
            s += lst[i] - x;
        }

        printf("%d\n", s);
    }

    return 0;
}
