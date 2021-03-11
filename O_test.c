#include <stdio.h>

int main()
{
    int i = 2;
    int j = 5;

    char *str = strcat(itoa(i), " haha " ,itoa(j));
    printf("%s", str);
    return 0;
}
