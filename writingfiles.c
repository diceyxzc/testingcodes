#include <stdio.h>

int main() {

    //creating file within desired folder.
    FILE *pF = fopen("C:\\Users\\fla10\\Desktop\\test.txt", "w"); //"a", add to file

    fprintf(pF, "AAAAAAAAAAAAAA");

    fclose(pF);

    if(remove("text.txt") == 0) {
        printf("File Deleted.");
    } else {
        printf("Not deleted.");
    } //delete file

    return 0;
}