#cybersecurity #hacking #penetration-testing 
#active-directory #man-in-the-middle #ipv6

# IPv6 Attacks

## IPv6 Attacks Overview

- using the fact that no one is managing DNS for IPv6

## Install Mitm6

Official repo: https://github.com/dirkjanm/mitm6
It comes with PMK: https://github.com/Dewalt-arch/pimpmykali

## Setting up LDAPS in AD Lab

This sets up LDAP Secure on the Server :

1. Add Active Directory Certificate Services to the DC
2. Configure with Certification Authority- keep all default settings except change validity period to 99 years

## IPv6 DNS Takeover via mitm6

1. Use mitm6

```bash
mitm6 -d dbz.local
```

![](https://i.imgur.com/vxPlb0g.png)

2. Start the relay attack pointed right at the DC

```bash
ntlmrelayx.py -6 -t ldaps://192.168.2.135 -wh fakewpad.dbz.local -l lootme
```
Notes: -6 for IPv6, -t for target, -wh (wtf is a wpad?), -l for loot

![](https://i.imgur.com/UjmjSh6.png)

3. Reboot the Win10-Vegeta Machine to speed things up

4. Output of the relay attack--->

This is the relay dumping the domain info:

![](https://i.imgur.com/P1vFSyJ.png)

Find passwords for the SQL Service!

![](https://i.imgur.com/mgMlMX6.png)

When an admin logins in to one of the win10 machines we get a new user created

![](https://i.imgur.com/HueOfR4.png)

If we check the Active Directory Users and Computers on Namek-DC

![](https://i.imgur.com/lzZvHSB.png)

### ACLPWN

It might be useful to know this is created in the mitm6 folder

![](https://i.imgur.com/QuKyeLu.png)

## Further information on IPv6

https://dirkjanm.io/worst-of-both-worlds-ntlm-relaying-and-kerberos-delegation/

## IPv6 Attack Defenses

Mitigation Strategies:

1. IPv6 poisoning abuses the fact that Windows queries for an IPv6 address even in IPv4-only environments. If you don't use IPv6 internally, the safest way to prevent mitm6 is to block DHCPv6 traffic and incoming router advertisements in Windows Firewall via Group Policy. Disabling IPv6 entirely may have unwanted side effects. Setting the following predefined rules to Block instead of Allow prevents the attack from working:

a. (Inbound) Core Networking - Dynamic Host Configuration
b.  (Inbound) Core Networking - Router Advertisement  
(ICMPv6-In)
c. (Outbound) Core Networking- Dynamic Host Configuration Protocol for IPv6 (DHCPV6-Out)

2. If WAD is not in use internally, disable it via Group Policy and by disabling the WinHttpAutoProxySvc service.
3.  ﻿﻿﻿Relaying to LDAP and LDAPS can only be mitigated by enabling both LDAP signing and LDAP channel binding
4.  ﻿﻿﻿Consider Administrative users to the Protected Users group or marking them as Account is sensitive and cannot be delegated, which will prevent any impersonation of that user via delegation.