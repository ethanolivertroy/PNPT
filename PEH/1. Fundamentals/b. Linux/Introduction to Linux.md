# Introduction to Linux

## Users and Privs

### CHMOD
![](https://i.imgur.com/MFc3Ky0.png)

## Starting and Stopping Services

```
sudo service apache2 start
```

```python
python3 -m http.sever 80
```

### want a service to run/stopwhen the system boots up?
Examples:
```
sudo systemctl enable ssh
```

```
sudo systemctl disable ssh
```

## Installing and Updating Tools

https://github.com/Dewalt-arch/pimpmykali

## Scripting with Bash

```bash
#!/bin/bash
if [ "$1" == "" ]
then
echo "You forgot an IP address!"
echo "Syntax: ./ipsweep.sh 192.168.1" else
for ip in `seq 1 254`; do 
ping -c 1 $1.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" & 
done
```

## Other Linux Notes

### Change to Root User
```
sudo su - 
```

### Print Working Directory
```
pwd
```

### Remove Directory
```
rmdir
```

https://explainshell.com/

--help

### List All
```
ls -la
```

### Copy
```
cp
```

### Move
```
mv
```

### Locate
```
locate
```

### Update Database to find shit
```
updatedb
```

```
grep
```

ip a, ip r

route, ping

netstat