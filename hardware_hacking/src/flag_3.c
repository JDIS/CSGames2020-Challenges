#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <unistd.h>

int main()
{
    struct Node {
        char value;
        int64_t offset;
    } nodes[28];

    const char payload[] = {0x02, 0x45, 0x10, 0x74, 0x6d, 0x18, 0x5d, 0x10, 0x44, 0x04, 0x70, 0x5e, 0x1e, 0x53, 0x16, 0x4d, 0x14, 0x61, 0x55, 0x1a, 0x57, 0x5, 0x5b, 0x14, 0x61, 0x44, 0x2b};
    const char key[] = {0x44, 0x09, 0x51, 0x33, 0x16, 0x56, 0x12};
    const char order[] = {14,  2,  8, 19,  25,  1, 22,  6, 16, 4, 20, 7, 15, 5, 10, 21,  17, 9, 11, 18, 26, 13, 23, 24, 12, 27, 3};

    char current_position = 0;
    for (char i = 0; i < 27; ++i)
    {
        nodes[current_position].value = key[i % 7] ^ payload[i];
        nodes[current_position].offset = sizeof(struct Node) * (order[current_position] - current_position);
        current_position = order[current_position];
    }

    nodes[27].value = 0; nodes[27].offset = 0;

    fprintf(stderr, "%p", (void*)(nodes));
    for (;;) sleep(100);

    return 0;
}
