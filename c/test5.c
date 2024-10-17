//No. 6
#include <stdio.h>

void userInput(int num[], int size);
int evenValue(int num[], int size, int even[], int *evenCount);
void displayEvenValue(int even[], int evenCount);

int main() {
    int num[5], even[5], evenCount = 0;

    userInput(num, 5);
    evenValue(num, 5, even, &evenCount);
    displayEvenValue(even, evenCount);
    
    return 0;
}

void userInput(int num[], int size){
    int i;
    for (i = 0; i < size; i++){
        printf("Number %d: ", i + 1);
        scanf("%d", &num[i]);
    }
}

int evenValue(int num[], int size, int even[], int *evenCount){
    int i;

    for (i = 0; i < size; i++) {
        if (num[i] % 2 == 0) {
            even[*evenCount] = num[i];
            (*evenCount)++;
        }
    }
}

void displayEvenValue(int even[], int evenCount){
    int i;
    printf("The Even Values are: ");
    for (i = 0; i < evenCount; i++){
        printf("%d ", even[i]);
    }
}