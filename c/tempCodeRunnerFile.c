//No. 6
#include <stdio.h>

void userinput(float num[], int size);
int largestValue(float num[], int size, float *largest);
void displaylargestValue(float largest);

int main() {
    float num[3], largest;

    userinput(num, 3);
    largestValue(num, 3, &largest);
    displaylargestValue(largest);
    
    return 0;
}

void userinput(float num[], int size){
    int i;
    for (i = 0; i < size; i++){
        printf("Number %d: ", i + 1);
        scanf("%f", &num[i]);
    }
}

int largestValue(float num[], int size, float *largest){
    int i;
    *largest = num[0];

    for (i = 1; i < size; i++) {
        if (num[i] > *largest) {
            *largest = num[i];
        }
    }
}

void displaylargestValue(float largest){
    printf("The largest value is %.2f", largest);
}