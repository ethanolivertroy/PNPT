#cybersecurity #hacking #penetration-testing   
#active-directory

# Creating the Active Directory Hacking Lab

## TCM Video Walkthrough
<iframe width="560" height="315" src="https://www.youtube.com/embed/xftEuVQ7kY0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## The lab consists of: 
- 1 Windows Server 2019 (NAMEK-DC): 192.168.2.135
- 2 Windows 10 Enterprise 
	- (planet) VEGETA: 192.168.2.137
	- EARTH: 192.168.2.138

## Setting Up a Bad Admin Account

==Service accounts should not be domain admins==

![](https://i.imgur.com/eZjNNaX.png)

Most domain controllers have file shares

```
setspn -a DBz-DC/SQLService.DBZ.local:60111 DBZ\SQLService
```


## Vegeta is Admin on both the Vegeta and Earth Machines

This is the set up for our relay attack

![](https://i.imgur.com/mfo883Z.png)


## Disable Windows Defender

Although it will come in handy for it to be on as well to learn how to exploit without metasploit

![](https://i.imgur.com/F2faqkY.png)

## Other Notes

- For the PNPT course, we disabled Microsoft Defender to learn the basics
- I'll have to look back into anti-virus evasion 
- <mark style="background: #FF5582A6;">Ensure that Windows 10 Boxes are visible to other devices by turning on network discovery and file sharing</mark>
- Install VMWare Tools to get full screen and better experience