#include <stdio.h>
#include <string.h>

//typedef char user[25]; basically turns "char" into whatever

typedef struct { //"struct" becomes "user" | basically nicknames
    char name[25];
    char password[12];
    int id;
} User;

int main() {

    User user1 = {"insanity", "crazy", 2389};
    User user2 = {"crazy", "insanity", 2382139};

    printf("%s\n", user1.name);
    printf("%s\n", user1.password);
    printf("%d\n", user1.id);
    printf("\n");
    printf("%s\n", user2.name);
    printf("%s\n", user2.password);
    printf("%d\n", user2.id);

    return 0;
}