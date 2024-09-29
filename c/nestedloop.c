#include <stdio.h>

int main() {

    int rows;
    int columns;
    char symbol;

    printf("\nEnter # of rows: ");
    scanf("%d", &rows);

    printf("Enter # of columns: ");
    scanf("%d", &columns);

    printf("Enter a symbol: ");
    scanf(" %c", &symbol); //add space in %c

    //test multiple parameters to run multiple operations.

    for(int i = 1; i <= rows; i++) {
        for (int j = 1; j <= columns; j++) {
            printf("%c", symbol);
        } //this loop must be finished first before the outer loop continues.
        printf("\n");
    }

    return 0;
}