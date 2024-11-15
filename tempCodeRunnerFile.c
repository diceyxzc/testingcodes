#include <stdio.h>
#include <math.h>

int main(){
    int n;

    factorial(int n);

    return 0;
}

int factorial(int n) {
    n = 3;
    
    if (n == 0) {
        return 1;  // Base case
    }
    return n * factorial(n - 1);  // Recursive case
}