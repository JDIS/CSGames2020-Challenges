#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <sys/uio.h>

int main()
{
    volatile pid_t process_id = 17;
    volatile size_t buffer_size = 40;
    void* buffer_addr = (void*)0x7ffbffffbc60;

    struct iovec local[1];
    struct iovec remote[1];
    local[0].iov_base = calloc(buffer_size, sizeof(char));
    local[0].iov_len = buffer_size;
    remote[0].iov_base = buffer_addr;
    remote[0].iov_len = buffer_size;

    ssize_t nread = process_vm_readv(process_id, local, 1, remote, 1, 0);
    if (nread == buffer_size)
    {
        char* buffer = (char*)local[0].iov_base;
        int keysize = (int)(buffer[0]);
        char* key = buffer + 1;
        int payloadsize = (int)(buffer[1+keysize]);
        char* payload = buffer + 2 + keysize;
        int i = 0;
        for (int j = 0; j < payloadsize; ++j)
        {
            putc(payload[j] ^ key[i], stderr);
            i = (i+1) % keysize;
        }
        putc('\n', stderr);

        return 0;
    }
    return 1;
}
