#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    const int MIN = 1;
    const int MAX = 100;
    int guess;
    int guesses;
    int answer;

    srand(time(0)); //uses current time to create random numbers

    answer = (rand() % MAX) + MIN; //generate a random number

    do{
        printf("Enter a guess: ");
        scanf("%d", &guess);
        if(guess > answer) {
            printf("Too High!\n");
        } else if(guess < answer) {
            printf("Too Low!\n");
        } else {
            printf("Correct!\n");
        }
        guesses++;
    }while(guess != answer);

    printf("---------------------");
    printf("\nAnswer: %d\n", answer);
    printf("Guesses: %d\n", guesses);
    printf("---------------------");

    return 0;
}