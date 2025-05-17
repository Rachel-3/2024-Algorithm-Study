a = input()
croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in range(8):
    a = a.replace(croatia[i], "_")

print(len(a))