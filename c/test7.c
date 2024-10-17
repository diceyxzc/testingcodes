//No. 9
#include <stdio.h>

void userInput(int num[], int size);
int sortValue(int num[], int size, int sort[], int *sortCount);
void displayDescendingOrder(int sort[], int sortCount);

int main() {
    int num[5], sort[5], sortCount = 0;

    userInput(num, 5);
    sortValue(num, 5, sort, &sortCount);
    displayDescendingOrder(sort, sortCount);
    return 0;
}

void userInput(int num[], int size){
    int i;
    for (i = 0; i < size; i++){
        printf("Number %d: ", i + 1);
        scanf("%d", &num[i]);
    }
}

int sortValue(int num[], int size, int sort[], int *sortCount){
    int i, j, check;

    for(i = 0; i < size - 1; i++){
        for(j = 0; j < size - i - 1; j++){
            if(num[j] < num[j + 1]){
                check = num[j];
                num[j] = num[j + 1];
                num[j + 1] = check;
            }
        }
    }
    
    for (i = 0; i < size; i++) {
        sort[i] = num[i];  
    }
    
    *sortCount = size;  
}

void displayDescendingOrder(int sort[], int sortCount){
    int i;
    printf("Sorted values in descending order:\n");
    for (int i = 0; i < sortCount; i++) {
        printf("%d ", sort[i]);
    }
}