import Boot_code
#import Partition
#import Signature

def MBR_parser(dir_addr):
    
    #MBR_Structure
    #1. Boot_Code (0 ~ 445 byte)
    #2. Partition (446 ~ 510 byte)
    #3. Signature (511 ~ 512 byte)

    with open(dir_addr, "rb") as f:
        Boot_code(f)
        
        #for i in range(4):
            #Partition(f, i+1)
        #Signature(f)
        
    f.close()