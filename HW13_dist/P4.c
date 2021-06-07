#include <stdio.h>
#include <stdlib.h>
#define MAX_NUMS 10

void InsertionSortReverse(char list[]);
int main(int argc, char* argv[])
{
  char chars[MAX_NUMS]; //List of characters to be sorted

  if (argc < MAX_NUMS){
    printf("Please give %d inputs\n", MAX_NUMS);
    return -1;
  }
  

  for (int index=0; index < MAX_NUMS; index++)
  {
    chars[index] = argv[index + 1][0];    
  }

  InsertionSortReverse(chars); //Call sorting routine

  //Print sorted list  
  for (int index = 0; index < MAX_NUMS; index++)
    printf("%c", chars[index]);
}

void InsertionSortReverse(char list[])
{
  /* Write your code here */
	
for(int i=0; i<10; i++){
  char tempval = list[i];
  int tempvalloc = i;
  for(int j = i+1; j<10; j++){
    if(tempval < list[j]){
      tempval = list[j];
      tempvalloc = j;
    }
  }
  if(tempvalloc != i){
    list[tempvalloc] = list[i];
    list[i] = tempval;
  }else{continue;}
}

  /*do not modify below*/
}
