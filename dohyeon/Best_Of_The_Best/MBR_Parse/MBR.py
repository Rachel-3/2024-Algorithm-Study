import Boot_code
import Partition
import Signature

def parser(dir_addr):
    
    #MBR_Structure
    #1. Boot_Code (0 ~ 445 byte)
    #2. Partition (446 ~ 510 byte)
    #3. Signature (511 ~ 512 byte)

    with open(dir_addr, "rb") as f:
        Boot_code.parsing(f)
        
        for i in range(4):
            Partition.parsing(f, i+1)
            print('\n')
        Signature.parsing(f)
        
    f.close()