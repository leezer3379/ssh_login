#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-4-7 上午9:02
# @Author  : Leezer3379
# @Site    : https://github.com/leezer3379
# @File    : my_paramiko.py
# @Software: PyCharm
import paramiko
host = '10.211.55.13'
user = 'root'
port = 22
passwd = 'huan@123'
## key
def ssh_key():
    print("key login")
    pkssh = paramiko.SSHClient()
    pkssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    key = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
    pkssh.connect(hostname=host, port=port, username=user, pkey=key)

    while True:
        if user == 'root':
            stdin, stdout, stderr = pkssh.exec_command('pwd')
            cmd = raw_input('root@gavin-virtual-machine:%s#' % stdout.read().strip())
        else:
            stdin, stdout, stderr = pkssh.exec_command('pwd')
            cmd = raw_input('%s@gavin-virtual-machine:%s$' % (user,stdout.read().strip()))
        if cmd == 'exit':
            pkssh.close()
            exit()
        stdin, stdout, stderr = pkssh.exec_command(cmd)

        if not stdout:
            print(stderr.read().strip())

        print(stdout.read().strip())

## pass
def ssh_passwd():
    print("passwd login")
    pkssh = paramiko.SSHClient()
    pkssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    pkssh.connect(hostname=host, port=port, username=user, password=passwd)

    while True:
        if user == 'root':
            stdin, stdout, stderr = pkssh.exec_command('pwd')
            cmd = raw_input('root@gavin-virtual-machine:%s#' % stdout.read().strip())
        else:
            stdin, stdout, stderr = pkssh.exec_command('pwd')
            cmd = raw_input('%s@gavin-virtual-machine:%s$' % (user,stdout.read().strip()))
        if cmd == 'exit':
            pkssh.close()
            exit()
        stdin, stdout, stderr = pkssh.exec_command(cmd)

        if not stdout:
            print(stderr.read().strip())

        print(stdout.read().strip())

def main():
    ssh_key()
    # ssh_passwd()


if __name__ == '__main__':
    main()