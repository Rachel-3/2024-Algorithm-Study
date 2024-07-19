import struct

def parsing(f, i):
    print("\n------ Partition #"+str(i)+" ------")
    Check_BootFlag(f)
    Start_CHS(f)
    Type_partition(f)
    End_CHS(f)
    Start_LBA(f)
    Size_Sector(f)
    
    
def Check_BootFlag(f):
    bootFlag = f.read(1)
    print(" - Boot Flag : ",end='')
    print(bootFlag,end='')
    if(bootFlag == b'\x80'):
        print(", 부팅 가능합니다.")
    elif(bootFlag == b'\x00'):
        print(", 부팅 불가능합니다.")
    else:
        print("값이 손상되었습니다.")


def Start_CHS(f):
    size_info = '0x' + struct.pack('<l',int(f.read(3).hex(),16)).hex()[:-2]
    print(" - start address of CHS : " + size_info)
    
def Type_partition(f):
    type_partition = f.read(1)
    print(" - Type of Partition : ",end='')
    print(type_partition,end='')
    
    if(type_partition == b'\x05'):
        print(", DOS 3.3+ 확장 파티션 입니다.")
    elif(type_partition == b'\x0f'):
        print(", 확장 LBA 파티션 입니다.")
    else:
        print(", 값이 손상되었습니다.")
    
    
def End_CHS(f):
    addr_info = '0x' + struct.pack('<l',int(f.read(3).hex(),16)).hex()[:-2]
    print(" - end address of CHS : " + addr_info)
    
def Start_LBA(f):
    addr_info = ''
    #addr_info = '0x' + struct.pack('<l',int(f.read(4).hex(),16)).hex()[:-2]
    print(" - start address of LBA : " + str(f.read(4)))
    return addr_info
    
def Size_Sector(f):
    size_info = ''
    size_info = '0x' + struct.pack('<l',int(f.read(4).hex(),16)).hex()[:-2]
    print(" - Size of Sector : " + str(int(size_info,16)*512) + "Kb")
