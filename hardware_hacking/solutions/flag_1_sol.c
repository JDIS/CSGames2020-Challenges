#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <sys/uio.h>

int main()
{
    volatile pid_t process_id = 13;
    volatile size_t buffer_size = 25;
    void* buffer_addr = (void*)0x7ffbffffbc90;

    struct iovec local[1];
    struct iovec remote[1];
    local[0].iov_base = calloc(buffer_size, sizeof(char));
    local[0].iov_len = buffer_size;
    remote[0].iov_base = buffer_addr;
    remote[0].iov_len = buffer_size;

    ssize_t nread = process_vm_readv(process_id, local, 1, remote, 1, 0);
    if (nread == buffer_size)
    {
        fprintf(stderr, "%s\n", local[0].iov_base);
        return 0;
    }
    return 1;
}
