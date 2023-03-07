#cybersecurity #hacking #penetration-testing 
#hack-the-box #metasploit #privilege-escalation 
#port80 
# Optimum Machine

## NMAP Results

![](https://imgur.com/Wl2bxSV.png)

## Enumeration

Port 80 was open so we go to the IP address to see what web content is being served.
We see the same HttpFileServer 2.3 here.
We could google this or just check metasploit.

![](https://i.imgur.com/aDkRNqc.png)

## Metasploit

### Find exploit for HttpFileServer 2.3
![](https://i.imgur.com/7CkFSTI.png)

### Configure the Options
![](https://i.imgur.com/MCARFwk.png)

### There's a Difference in Architecture between the box and our meterpreter session
#### But that doesn't seem to affect our exploitation
Possible because Metasploit is auto-detecting the target
![](https://i.imgur.com/t90ygyX.png)

### Privilege Escalation

I background the first meterpreter session and search for suggested post-breach exploits
The only option that needs to be configured here is the session
If sessions aren't know you can just run ```show sessions```

![](https://i.imgur.com/eYt9OL7.png)

Once the suggester runs, I find what I'm really looking for which is a way to ==privilege escalate== from the "Kostas" user to the system authority/root

![](https://i.imgur.com/SIwd2Ix.png)

We get system authority from the exploit

![](https://i.imgur.com/XwOKt8T.png)

## Manual Exploitation

Work thru this again without metasploit.

## To Reference Later

<iframe width="560" height="315" src="https://www.youtube.com/embed/kWTnVBIpNsE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/bTxnobhJ_b8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

- https://0xdf.gitlab.io/2021/03/17/htb-optimum.html
- 