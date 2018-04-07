# get hostname
cat /etc/issue
hostname
/etc/redhat-release

# get mac address

cat /sys/class/net/ens*/address

cat /sys/class/net/eth*/address
### best good
cat /sys/class/net/[^vtlsb]*/address

# 硬件机型
### 制造商
root@gavin-virtual-machine:/home/gavin# dmidecode -s system-manufacturer
VMware, Inc.
### 具体型号
root@gavin-virtual-machine:/home/gavin# dmidecode -s system-product-name
VMware Virtual Platform
### 序列号
dmidecode -s chassis-serial-number

yum -y install dmidecode          or        apt-get install dmidecode -y