#include <stdio.h>

void insanity(char x[], int y) {
    printf("YOU WERE %s in between the %d!\n", x, y); 
    printf("YOU WERE %s in between the %d!\n", x, y);
    printf("YOU WERE %s in between the %d!\n", x, y);
}

int main() {
    char name[] = "Insanity";
    int age = 41;

    insanity(name, age);

    return 0;
}