#include<stdio.h>
#include<fcntl.h>
#include <dirent.h>
#include<sys/types.h>
int main(int argc,char* argv[])
{
  DIR *d;
  struct dirent *dir;
  char*dirname;
  d=opendir(argv[1]);
   int i=0;
  //d=opendir("/rohini/study-material");
  //printf("\n enter dir");
  //scanf("%s",dirname);
  //d=opendir(dirname);
  if(d == NULL)
   {
    printf("\n not open\n");
   }
  else
  {
   printf("\n  is open sucessfullly\n");
   while((dir =readdir(d))!=NULL)
    {
     i++;
     printf("\n%s",dir->d_name);
    }
    printf("\n\nreaddir() found a total of %i files\n",i);
   if (closedir(d)==-1)
   {
    perror("closeddir");
    return 0;
   }
  }
  
   
  return 0;
}

  
