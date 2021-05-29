#include <stdio.h>
#include <stdlib.h>

// Implement P2 
// You can define other function, but P2 must return answer.
int P2_helper(int x, int y){
    if (y == 0) {
		return x;
	}
	else {
		return P2_helper(y, x % y);
	}
}
int P2(int n){
    int x;
    if(n==1){
        x=1;
        return 1;
    }else{
    x = n*P2(n-1)/P2_helper(n, P2(n-1));
    return x;
    }
}
// DO NOT MODIFY BELOW!
int main(int argc, char* argv[]){
    int n = atoi(argv[1]);
    int ans = P2(n);

    printf("%d\n", ans);

    return 0;
}