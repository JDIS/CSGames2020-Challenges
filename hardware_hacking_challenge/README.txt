Welcome to this hardware hacking challenge !

In this docker container, you should be able to retrieve 2 flags.

Flag 1
------

The first flag is contained in the memory of the process named flag_1 at address __FLAG_1_ADDR__. It's a null terminated string so don't search too hard !

HINT: http://man7.org/linux/man-pages/man2/process_vm_readv.2.html

Flag 2
------

The second flag is contained in the memory of the process named flag_2 at address __FLAG_2_ADDR__. Although this time, there is a protocol to follow:

The buffer is composed of two packets. Each packets follow the same length-value encoding scheme. The first byte of the packet is the header and represents the length in bytes of the packet's data.

The first packet's data is a key. The second packet's data is a cipher. Good luck !
