//No. 8
#include <stdio.h>

void userInput(int *num1, int *num2);
int calculatingGDC(int num1, int num2, int *result);
void displayGDC(int num1, int num2, int result);

int main() {
    int num1, num2, result;

    userInput(&num1, &num2);
    result = calculatingGDC(num1, num2, &result);
    displayGDC(num1, num2, result);
    return 0;
}

void userInput(int *num1, int *num2){
    printf("Enter 1st Number: ");
    scanf("%d", num1);

    printf("Enter 2nd Number: ");
    scanf("%d", num2);
}

int calculatingGDC(int num1, int num2, int *result){
    int temp;
    
    //Euclidean Algorithm
    if (num1 < 0) num1 = -num1;
    if (num2 < 0) num2 = -num2;

    while (num2 != 0){
        temp = num2;
        num2 = num1 % num2;
        num1 = temp;
    }

    return num1;
}

void displayGDC(int num1, int num2, int result){
    printf("The GDC of %d and %d is %d.", num1, num2, result);
}