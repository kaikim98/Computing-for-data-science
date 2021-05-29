/* Description
 * Write a program that reads any english alphabet from the keyboard 
 * and prints every character from that character down 
 * to the character A in the order in which they appear in the ASCII table
 */

#include <stdio.h>

void main(int argc, char* argv[]){
	/* Please write your code below */
	char ans;

	printf("Enter any alphabet:");
	scanf("%c", &ans);
	int alphabet = (int)ans;

	while(alphabet > 64){
		char c_alpha = (char)alphabet; 
		printf("%c", alphabet);
		alphabet -= 1;
	}

	/* Do not modify below */
}

