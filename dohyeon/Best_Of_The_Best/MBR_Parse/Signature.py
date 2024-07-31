def parsing(f):
    sign = f.read(2)
    
    print(" - MBR Signature : ",end='')
    if(sign == b'\x55\xAA'):
        print(sign)
    else:
        print("시그니처 값이 훼손되었습니다.")