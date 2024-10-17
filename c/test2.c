//No. 4
#include <stdio.h>

int userInput();
void equiGrade(int num1);

void main() {
    int num1;

    num1 = userInput();
    equiGrade(num1);
}

int userInput(){
    int num1;

    printf("Enter Grade: ");
    scanf("%d", &num1);

    return num1;
}

void equiGrade(int num1){
    if (num1 >= 90) {
        printf("A! - Excellent");
    } else if (num1 >= 75){
        printf("B! - Good");
    } else {
        printf("C! - Poor");
    }
}