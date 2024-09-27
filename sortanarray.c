#include <stdio.h>

void sort(char array[], int size) { //char array[] | int array[]
    
    for(int i = 0; i < size - 1; i++) { 
        for(int j = 0; j < size - i - 1; j++){ //checks if size is greater than 0 for loop to run.
            
            if(array[j] > array[j+1]) { //checks if number is greater than the next number.
                int temp = array[j]; //basic integer switch.
                array[j] = array[j+1];
                array[j+1] = temp;

            }
        }
    }
}

void printarray(char array[], int size) { //char array[] | int array[]
    for (int i = 0; i < size; i++) {
        printf("%c ", array[i]);
    }
}

int main() {

    //int array[] = {9, 3, 4, 5, 1, 7,};
    char array[] = {'F', 'S', 'T', 'G', 'H', 'I'};
    int size = sizeof(array)/sizeof(array[0]);

    sort(array, size);
    printarray(array, size);

    return 0;
}