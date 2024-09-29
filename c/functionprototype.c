#include <stdio.h>

void hello(char[], int); //function prototype

int main() {

    char name[] = "Calvin";
    int age = 19;

    hello(name, age);

    return 0;
}

void hello(char name[], int age) {
    printf("Hello %s\n", name);
    printf("You are %d years old.", age);
}