#include <stdio.h>

int main() {

    for(int i = 1; i <= 20; i++) {
        
        /*if(i == 13) {
            continue; //removes a certain condition.
        } */
        
        if(i == 13){
            break; //stops at the condition.
            
        }
        printf("%d\n", i);
    }

    return 0;
}