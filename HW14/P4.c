#include <stdio.h>
char P4_helper();
int P4_primenum();
int main(int argc, char *argv[]){    
    char *input_filename = argv[1]; // name of input file
    char *output_filename = argv[2]; // name of output file
    // YOUR CODE HERE
    FILE *infile;
    FILE *outfile;
    int num;

    infile = fopen(input_filename, "r");
    outfile = fopen(output_filename, "w");
    while(fscanf(infile, "%d", &num)!=EOF){
        if(P4_primenum(num) == -1){
            char result = P4_helper(num);
            fprintf(outfile, "%s\n", result);
        }else{
            fprintf(outfile, "%s\n", num);
        }
    }
    return 0;
}

char P4_helper(int num){
    char str[50];
    str[0] = num;
    str[1] = "=";
    int loc = 2;
    for(int i=2; i<num/2; i++){
        if(n%i==0){
            n /= i;
        }
    }
}

