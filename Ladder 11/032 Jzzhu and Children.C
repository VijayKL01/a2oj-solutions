#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int index;
    int value;
} Pair;

int compare(const void *a, const void *b) {
    Pair *pa = (Pair *)a;
    Pair *pb = (Pair *)b;
    return pa->value - pb->value;
}

int main() {
    int n, m, input, f, i = 0, l = 0;
    Pair vect[1000]; // Assuming a maximum of 1000 elements

    scanf("%d %d", &n, &m);

    for (int i = 0; i < n; i++) {
        scanf("%d", &input);
        vect[i].index = i + 1;
        vect[i].value = input;
    }

    qsort(vect, n, sizeof(Pair), compare);

    if (n == 1) {
        l = 1;
    } else {
        while (n > 1) {
            if (m >= vect[0].value) {
                n--;
            } else {
                vect[0].value -= m;
                vect[n++] = vect[0];
                n--;
            }
        }
    }

    printf("%d\n", vect[0].index);

    return 0;
}
