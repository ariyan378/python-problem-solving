#include<stdio.h>

int main(){
    


  int x1,x2, result;
  printf("Enter your X1 and X2 :\n");
  scanf("%d%d",&x1,&x2);
  printf("X1 = %d\n",x1);
  printf("X2 = %d\n",x2);

  printf("Additon ---- 1\n");
  printf("Multiplication---2\n");
  printf("subtraction ---- 3\n");
  printf("division---4\n");
  
  int choice;
  printf(" Enter a number between 1-4 : ");
  scanf("%d",&choice);

  if (choice==1){
    result = x1+x2;
    printf("result : %d" , result);
  }else if (choice==2)
  {
    /* code */
    result = x1*x2;
    printf("result : %d" , result);
  }else if (choice==3)
  {
    /* code */
    result = x1-x2;
    printf("result : %d" , result);
  }else if(choice==4){
    result = x1/x2;
    printf("result : %d" , result);
  }
  
  
  return 0;

}