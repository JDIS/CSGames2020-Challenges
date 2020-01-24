#!/bin/bash

timeout 0.5 strace -p 1 &> /dev/null
if [ $? -ne 124 ]
then
    echo "PTRACE not enabled ... you should run docker with the start script !"
    exit 1
fi

for i in {1..3}
do
  /opt/flag_$i 2> /root/.f${i}addr &
  sleep 0.3
  sed -i "s/__FLAG_${i}_ADDR__/$(cat /root/.f${i}addr)/g" /root/README.txt
done
