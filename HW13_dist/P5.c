#include <stdio.h>
#include <stdlib.h>
#define MAX_LEN 10

char *SwitchCase(char *s);
int main(int argc, char* argv[])
{
  char *str; //List of characters to be sorted

  str = argv[1];
  printf("%s", SwitchCase(str));

}
/* Do not modify above */
/* Write your code below */
char *SwitchCase(char *s){
  int i;
  for(i=0; i<10; i++){
    if((s[i]>='a')&&(s[i]<='z')){
      s[i] = s[i]-32;
    }
    else if((s[i]>='A')&&(s[i]<='Z')){
        s[i] = s[i]+32; 
    }
  }return s;
}