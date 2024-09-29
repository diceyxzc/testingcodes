#include <stdio.h>
#include <ctype.h>

int main() {

    char questions[][100] = {"1.) Dogs or Cats? ",
                            "2.) Insanity or Crazy? ",
                            "3.) Water or watuh? "};
    
    char options[][100] = {"A. Dogs", "B. Cats",
                            "A. Insanity", "B. Crazy",
                            "A. Water", "B. Watuh"};
    
    char answers[3] = {'A', 'A', 'B'};
    int numberOfQuestions = sizeof(questions)/sizeof(questions[0]);

    char answer;
    int score;

    printf("Quiz Game\n");

    for(int i = 0; i < numberOfQuestions; i++) {
        printf("----------------------\n");
        printf("%s\n", questions[i]);
        printf("----------------------\n");

        for(int j = (i * 2); j < (i * 2) + 2; j++) {
            printf("%s\n", options[j]);
        }

        printf("Answer: ");
        scanf(" %c", &answer); //space to clear input buffer.

        answer = toupper(answer);

        if(answer == answers[i]) {
            printf("CORRECT!\n");
            score++;
        } else {
            printf("WRONG!\n");
        }
    }

    printf("----------------------\n");
    printf("FINAL SCORE: %d/%d\n", score, numberOfQuestions);
    printf("----------------------\n");

    return 0;
}