//No. 5
#include <stdio.h>

void userinput(int *num1);
void conversion(int num1, int *result);
void displayConversion(int num1, int result);

void main() {
    int num1, num2, result;

    userinput(&num1);
    conversion(num1, &result);
    displayConversion(num1, result);
}

void userinput(int *num1){
    printf("Enter a Kilometer to Convert into Meters: ");
    scanf("%d", num1);
}

void conversion(int num1, int *result){
    *result = num1 * 1000;
}

void displayConversion(int num1, int result){
    printf("%d Kilometers is %d meters.", num1, result);
}