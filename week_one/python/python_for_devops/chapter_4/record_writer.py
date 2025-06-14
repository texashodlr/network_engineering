dd if=/dev/zero of=/dev/sdc count=10 bs=100M

# It writes 10 records of 100MB at a rate of 1GB/s-- this is throughput!

# IOPS with dd is iostat, verify the above with: 
iostat -d /dev/sdc 1

# Can also run:
while true; do clear && iostate -d /dev/sdc && sleep 1; done

# fio -- try it out as well-- very powerful!

# fdisk ~ parted wbut with a different interface, can script parted with:

parted --script /dev/sdaa mklabel gpt
parted --script /dev/sdaa mkpart primary 1 40%
parted --script /dev/sdaa print

# Viewing disk information with:
blkid /dev/sda
lsblk /dev/sda

# SSH Tunneling
ssh -L 9998:localhost:15672 -p 2223 \
username@server -N

# -L is the flag that signals that we want forwarding enabled and a local port (9998) to bind to a remote port (default is 15672)
# -p indicates that the custom ssh port of the remote server is 2223
# user and addr are specified then the -N means that it should get us to a remote shell and do the forwarding
# Useful flag is '-f' it will send the process into the background, leaving the terminal ready and clean to do more work

# Apache Benchmark tool
ab -c 100 -n 10000 http://localhost/

# This creates 100 requests at a time for a total of 10,000 requests to a local instance where something (NGINX) is running

# Great command for seeing overall cpu utilization

ps -eo pcpu,pid,user,args | sort -r | head -10


