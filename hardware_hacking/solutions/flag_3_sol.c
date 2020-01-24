#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <sys/uio.h>
#include <stdint.h>

int main()
{
    struct Node {
        char value;
        int64_t offset;
    };

    volatile pid_t process_id = 21;
    volatile size_t buffer_size = sizeof(struct Node);
    void* buffer_addr = (void*)0x7ffbffffbae0;

    struct iovec local[1];
    struct iovec remote[1];
    local[0].iov_base = calloc(buffer_size, sizeof(char));
    local[0].iov_len = buffer_size;
    remote[0].iov_base = buffer_addr;
    remote[0].iov_len = buffer_size;

    for (;;)
    {
        ssize_t nread = process_vm_readv(process_id, local, 2, remote, 1, 0);
        if (nread != buffer_size)
            return 1;
        struct Node* buffer = (struct Node*)local[0].iov_base;
        putc(buffer->value, stderr);
        if (buffer->value == 0)
        {
            putc('\n', stderr);
            return 0;
        }
        buffer_addr = (void*)((uint64_t)buffer_addr + buffer->offset);
        remote[0].iov_base = buffer_addr;
    }

    return 1;
}
