#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main()
{
    const char payload[] = {0x46, 0x4c, 0x41, 0x47, 0x7b, 0x54, 0x48, 0x49, 0x53, 0x49, 0x53, 0x45, 0x41, 0x53, 0x59, 0x4d, 0x45, 0x4d, 0x43, 0x50, 0x59, 0x7d, 0x00};
    fprintf(stderr, "%p", (void*)payload);
    for (;;) sleep(100);

    return 0;
}