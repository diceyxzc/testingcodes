#include <stdio.h>

enum day{Sun = 1, Mon = 2, Tue = 3, Wed = 4, Thu = 5, Fri = 6, Sat = 6};

int main() {

    enum day today = Mon;

    //printf("%d", today);

    if(today == Sun || today == Sat) {
        printf("It's the weekend!");
    } else {
        printf("AAAAAAAAAAAA");
    }
    return 0;
}