#include <stdio.h>
#include <string.h>

int main() {

    char name[25];

    printf("\nEnter name: ");
    fgets(name, 25, stdin);
    name[strlen(name) - 1] = '\0';
    
    //only needed if an incorect input is given | checks a condition first.
    
    /*while(strlen(name) == 0) {
        printf("You did not enter your name");
        printf("\nEnter name: ");
        fgets(name, 25, stdin);
        name[strlen(name) - 1] = '\0';
    } */

    while(strcmp(name,"Calvin") == 0) {
        printf("You entered the correct name.");
        return 0;
    }
    
    printf("Hello %s", name);

    return 0;
}