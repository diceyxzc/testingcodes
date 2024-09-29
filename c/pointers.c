#include <stdio.h>

void printAge(int *pAge) {
    printf("You are %d", *pAge);
}

int main() {

    int age = 19;
    int *pAge = NULL; //"*pAge" is the value at address.
    pAge = &age;

    printf("adress of age: %p\n", &age);
    printf("value of pAge: %p\n", pAge);

    printf("size of age: %d\n", sizeof(age));
    printf("size of pAge %d\n", sizeof(pAge));
    
    printf("value of age: %d\n", age);
    printf("value at stored address: %d\n", *pAge);

    printAge(pAge);

    return 0;
}