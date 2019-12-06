#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <sys/uio.h>

int main()
{
    volatile pid_t PID = 13;
    volatile size_t SIZE = 25;
    void* ADDR = (void*)0x7ffbffffbc90;

    struct iovec local[1];
    struct iovec remote[1];
    local[0].iov_base = calloc(SIZE, sizeof(char));
    local[0].iov_len = SIZE;
    remote[0].iov_base = ADDR;
    remote[0].iov_len = SIZE;

    ssize_t nread = process_vm_readv(PID, local, 2, remote, 1, 0);
    if (nread == SIZE)
    {
        fprintf(stderr, "%s\n", local[0].iov_base);
        return 0;
    }
    return 1;
}
