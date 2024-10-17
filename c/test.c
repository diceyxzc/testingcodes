//No. 3
#include <stdio.h>

void userinput(int *num1, int *num2);
void fact(int num1, int num2, long *factorial1, long *factorial2, long *factorial3);
float output(long factorial1, long factorial2, long factorial3);
void displayResult(int num1, int num2, float result);

int main() {
    int num1, num2;
    long factorial1, factorial2, factorial3;
    float result;

    userinput(&num1, &num2);
    fact(num1, num2, &factorial1, &factorial2, &factorial3);
    result = output(factorial1, factorial2, factorial3);
    displayResult(num1, num2, result);

    return 0;
}

void userinput(int *num1, int *num2){
    do {
        printf("Enter the value of N (N > M): ");
        scanf("%d", num1);

        printf("Enter the Value of M (Not Equal to 0): ");
        scanf("%d", num2);

        if (*num2 == 0){
            printf("[M Should Not Equal to 0.]\n");
        }
        
        if(*num1 <= *num2){
            printf("[Error: N should be greater than M.]\n");
        }
        
    } while(*num1 <= *num2 || *num2 == 0);
}

void fact(int num1, int num2, long *factorial1, long *factorial2, long *factorial3){
    *factorial1 = 1;
    *factorial2 = 1;
    *factorial3 = 1;
    int i, subtract = num1 - num2;
    
    for (i = 1; i <= num1; i++){
        *factorial1 *= i;
    }
    
    for (i = 1; i <= num2; i++) {
        *factorial2 *= i;
    }
    
    for (i = 1; i <= subtract; i++){
        *factorial3 *= i;
    }
}

float output(long factorial1, long factorial2, long factorial3){
    float result = factorial1 / (factorial2 * factorial3);
    return result;
}

void displayResult(int num1, int num2, float result){
    printf("The Combination of %d and %d: %.2f", num1, num2, result);
}