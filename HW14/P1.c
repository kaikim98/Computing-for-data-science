#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]){
    int N = atoi(argv[1]);
    // YOUR CODE HERE
    for(int i=0; i<N; i++){
        for(int j=i; j<N-1; j++){
            printf(" ");
        }
        for(int j=0; j<=2*i; j++){
            printf("*");
        }
        if(i<N-1){
            printf("\n");
        }
    }
    return 0;

}