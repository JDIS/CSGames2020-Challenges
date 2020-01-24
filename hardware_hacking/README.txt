Welcome to this hardware hacking challenge !

In this docker container, you should be able to retrieve 3 flags. Each flag can be obtained independently.

Flag 1
------

The first flag is contained in the memory of the process named flag_1 at address __FLAG_1_ADDR__. It's a null terminated string so don't search too hard !

HINT: http://man7.org/linux/man-pages/man2/process_vm_readv.2.html

Flag 2
------

The second flag is contained in the memory of the process named flag_2 at address __FLAG_2_ADDR__. Although this time, there is a protocol to follow:

The buffer is composed of two packets. Each packets follow the same length-value encoding scheme. The first byte of the packet is the header and represents the length in bytes of the packet's data.

The first packet's data is a key. The second packet's data is a ciphertext. Good luck !

HINT: It's a reciprocal cipher

Flag 3
------

The third flag is contained in a linked list starting at address __FLAG_3_ADDR__ of process flag_3. Each node of the list is defined as:

struct Node {
    char value;
    int64_t offset;
};

The offset is defined as the number of bytes between the current node and the next one. This number can be negative. Concatenate the values until your string is null-terminated. Have fun!

HINT: https://en.wikipedia.org/wiki/Linked_list
