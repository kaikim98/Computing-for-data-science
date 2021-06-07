#include <stdio.h>

int main(int argc, char *argv[]){    
    char *input_filename = argv[1]; // name of input file
    char *output_filename = argv[2]; // name of output file
    // YOUR CODE HERE
    FILE *infile;
    FILE *outfile;
    char str[50];

    infile = fopen(input_filename, "r");
    outfile = fopen(output_filename, "w");
    while(fscanf(infile, "%s", str)!= EOF){
        char num[50];
        for(int i=0; i < 13; i++){
            char num[50];
            if(i==3 | i==8){
                num[i] = '-';
            }else if(i<3){
                num[i] = str[i];
            }else if(i > 3 && i <8 ){
                num[i] = str[i-1];
            }else{
                num[i] = str[i-1];
            }
            }
            fprintf(outfile, "%s\n", num);
        }

    return 0;
}
