#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// Implement P3
// You can define other function, but P3 must return answer.
int P3(int n){
    int count;
    int i=n;
    int y=2*n;
    for(i;i<y;i++){
        for(int j=2; j<i/2; j++){
            if(i%j==0){
                count +=1;
                break;
            }
        }
    }


    int ans = n-count;
    return ans;
}

// DO NOT MODIFY BELOW!
int main(int argc, char* argv[]){
    int n = atoi(argv[1]);
    int ans = P3(n);

    printf("%d\n", ans);

    return 0;
}