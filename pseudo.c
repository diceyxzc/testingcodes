#include <stdio.h>
#include <stdlib.h>
#include <time.h>

//random numbers

int main() {

      srand(time (0));

      int number1 = (rand() % 20) + 1;
      int number2 = (rand() % 20) + 1;
      int number3 = (rand() % 20) + 1;

      printf("%d\n", number1);
      printf("%d\n", number2);
      printf("%d\n", number3);

    return 0;
}