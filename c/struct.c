#include <stdio.h>
#include <string.h>

struct Players{
    char name[12];
    int score;
};


int main() {

    struct Players player1;
    struct Players player2;

    strcpy(player1.name, "insanity");
    player1.score = 4;

    strcpy(player2.name, "crazy");
    player1.score = 5;

    printf("%s\n", player1.name);
    printf("%d\n", player1.score);
    
    printf("%s\n", player2.name);
    printf("%d\n", player2.score);

    return 0;
}