#include <stdio.h>
#include <string.h>

struct student {
    char name[12];
    float gpa;
};

int main() {
    struct student student1 = {"Calvin", 3.0};
    struct student student2 = {"insanity", 4.0};
    struct student student3 = {"crazy", 1.0};
    struct student student4 = {"oblivious", 2.0};

    struct student students[] = {student1, student2, student3, student4};

    for(int i = 0; i < sizeof(students)/sizeof(students[0]); i++) {
        printf("%-12s\t", students[i].name); //this is basically a tab, "-12s" is space
        printf("%.2f\n", students[i].gpa);
    }

    return 0;
}