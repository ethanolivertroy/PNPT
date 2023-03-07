#active-directory 

# Gaining Shell Access with a Credential

## Steps to Gaining Shell Access with a Credential

1. Boot up metapsloit ``msfconsole``
2. Search for ``psexec``
![](https://i.imgur.com/ftkVN6G.png)
3. ``windows/smb/psexec``
4. Update options
![](https://i.imgur.com/6R0AR60.png)

5. run ``windows/smb/psexec`` but it fails

![](https://i.imgur.com/mCHSzJS.png)

Attempting to gain a shell, the victim machine windows security picks it up.
How can we evade this?

![](https://i.imgur.com/MsHmVY1.png)

6. Try psexec.py by itself without Metasploit

Remember to put the password in ‘...' since I have a "!"

![](https://i.imgur.com/cQxcpyQ.png)

This works for us to gain a shell but there are other options as well:
- smbexec.py
- wmiexec.py

![](https://i.imgur.com/qSO6Cgw.png)

## Notes:
- start with smbexec or wmiexec
- psexec is very noisy
- start as quiet as possible