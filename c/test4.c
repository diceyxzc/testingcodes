//No. 6
#include <stdio.h>

void userinput(float num[], int size);
int smallestValue(float num[], int size, float *smallest);
void displaySmallestValue(float smallest);

int main() {
    float num[3], smallest;

    userinput(num, 3);
    smallestValue(num, 3, &smallest);
    displaySmallestValue(smallest);
    
    return 0;
}

void userinput(float num[], int size){
    int i;
    for (i = 0; i < size; i++){
        printf("Number %d: ", i + 1);
        scanf("%f", &num[i]);
    }
}

int smallestValue(float num[], int size, float *smallest){
    int i;
    *smallest = num[0];

    for (i = 1; i < size; i++) {
        if (num[i] < *smallest) {
            *smallest = num[i];
        }
    }
}

void displaySmallestValue(float smallest){
    printf("The smallest value is %.2f", smallest);
}