#include <stdio.h>

void getuserinput(int *num1, int *num2);
void getsum(int *num1, int *num2, int *sum);
void displayoutput(int num1, int num2, int sum);

int main() {
    int num1, num2, sum;
    
    getuserinput(&num1, &num2);
    getsum(&num1, &num2, &sum);
    displayoutput(num1, num2, sum);
    
    return 0;
}

void getuserinput(int *num1, int *num2){
    printf("Enter 1st Number: ");
    scanf("%d", num1);

    printf("Enter 2nd Number: ");
    scanf("%d", num2);
}

void getsum(int *num1, int *num2, int *sum){
    *sum = *num1 + *num2;
}

void displayoutput(int num1, int num2, int sum){
    printf("The sum of %d and %d is %d\n", num1, num2, sum);
}
