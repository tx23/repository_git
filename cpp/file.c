#include <unistd.h> 
#include <stdio.h>
int main() {
    chdir(“../shell”);
    printf(“current working directory: %s\n”,getcwd(NULL,0)); 
    return 0;
}
