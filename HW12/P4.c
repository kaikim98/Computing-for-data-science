#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int P4(int n);

// Implement P4 
// You can define other function, but P4 must return answer.
int P4(int n){
    int b = 0;
    int y = 2*n;
    bool isin = true;
    int x = n+1;
    while(isin){
    
        for (int i = x/2; i<=y; i++){
            int z = i;
            int c = 0;
            if(i==y){
                return x;
            }
            while (z>0){
                c += z%10;
                z /= 10;
            }
            if(c + i == x){
                break;
            }
        } 
        x++;
        y=2*x;
    }
}


// DO NOT MODIFY BELOW!
int main(int argc, char* argv[]){
    int n = atoi(argv[1]);
    int ans = P4(n);

    printf("%d\n", ans);

    return 0;
}