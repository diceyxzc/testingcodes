#include <stdio.h>

int main() {

    double prices[] = {5.0, 6.7, 6.3, 5.7, 4.3, 4, 0.5};

    //sizedof is literally bytes, it will update the array up until it reaches the limit.

    for(int i = 0; i < sizeof(prices)/sizeof(prices[0]); i++) { 
        printf("%.2lf\n", prices[i]);
    }

    return 0;
}