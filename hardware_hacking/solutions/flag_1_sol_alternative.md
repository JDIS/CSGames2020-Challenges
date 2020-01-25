# Second solution for hardware hacking flag # 1

```
# Step 1
# Resolve the pid of process flag_1
ps -aux |grep -i flag       
> root 13 (...) /opt/flag_1

# Step 2
# Figure out the address range for the stack
cat /proc/13/maps | grep -i stack 
> 7fff11bb4000-7fff11bd5000 (...) [stack]

# Step 3
# Dump stack of process id 13 to /tmp/mem_dump
apt install gdb
gdb --pid 13 -ex "dump memory /tmp/mem_dump 0x7fff11bb4000 0x7fff11bd5000" -ex "set confirm off" -ex "quit"

# Step 4
# Get the flag
cat /tmp/mem_dump | strings | grep -i flag
```
