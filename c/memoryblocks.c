#include <stdio.h>

int main () {

    // memory (street)
    // memory block (person)
    // memory address (house address)

    char a;
    double b[3];
    
    printf("%d bytes\n", sizeof(a));
    printf("%d bytes\n", sizeof(b));

    printf("%p\n", &a);
    printf("%p\n", &b);

    return 0;
}