#include <stdio.h>

int main() {
    
    int number = 0;
    int sum = 0;
    
    //does an operation before it stops because a condition is met.

    do {
        printf("Enter a number above 0: ");
        scanf("%d", &number);
        
        if(number > 0) {
            sum += number;
        }

    } while(number > 0);

    printf("sum: %d", sum);

    return 0;
}