#include <stdio.h>

int findMax(int x, int y) {
    
    return (x > y) ? x : y;
}

int main() {
    int max = findMax(6, 5);

    printf("%d", max);

    return 0;
}