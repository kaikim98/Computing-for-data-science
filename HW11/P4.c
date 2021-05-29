/* Description
 * Write a function to return an natural number in base 4
 * (using only the digits 0,1,2,3) 
 */

#include <stdio.h>
#include <stdlib.h>
/* Please write your code below */	
int base_four(int x){
	int ans = 0;
	int n = x % 4;
	x /= 4;
	ans += n;
	if(x>0){
		ans += 10 * base_four(x);
	}
	return ans;
}
/* Do not modify below */

void main(int argc, char* argv[]){

	if (argc != 2){
		printf("Enter any natural number n\n");
	}

	int n = atoi(argv[1]);		

	if (n < 0){
		printf("No negative number is allowed\n");
	}

	int f = 0;

	f = base_four(n);
	printf("%d\n",f);	
}

