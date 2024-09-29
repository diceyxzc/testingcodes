#include <stdio.h>
#include <string.h>

int main() {
    char string1[] = "Insanity";
    char string2[] = "Crazy";

    //strlwr(string1); //lowercase
    //strupr(string2); //uppercase
    //strcat(string1, string2); //combine strings
    //strncat(string1, string2, 2); //depends on how many u want to combine
    //strcpy(string1, string2); //switches str1 to str2
    //strncpy(string1, string2, 1); //given amount of characters
    
    //strset(string1, 'x'); //switches string1 to desired text
    //strnset(string1, 'p', 3); //depends on how much u want to set
    //strrev(string1); //reverses string

    //int result = strlen(string1); //counts how many characters
    //int result = strcmp(string1, string2); //compares characters
    //int result = strncmp(string1, string2, 1); //left to right, compares nth characters
    //int result = strcmpi(string1, string2); //ignores capital
    int result = strnicmp(string1, string2, 1); //ignores capital

    //printf("%s", string1);
    //printf("%d", result);

    if(result == 0) {
        printf("These strings are the same");
    } else {
        printf("These strings are not the same");
    }

    return 0;
}