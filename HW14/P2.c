#include <stdio.h>

int main(int argc, char *argv[]){
    char *input_filename = argv[1]; // name of input file
    // YOUR CODE HERE
    FILE *infile;
    infile = fopen(input_filename, "r");
    int answer = 0;
    int asdf;
    while (fscanf(infile, "%d", &asdf) != EOF){
        answer += asdf;
    }
    printf("%d", answer);
    return 0;
}