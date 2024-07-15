#include <stddef.h> // for size_t
#include <stdint.h> // for uint8_t
#include <stdio.h> // for printf~
#include <arpa/inet.h>

int isvalidbytes(int bytes1, int bytes2){
    if (bytes1 <= 0 || bytes2 <= 0) {
        printf("File size is low..\n");
        return 0;
    }
    return 1;
}

int main(int argc, char *argv[]) {
    if (argc != 3) {
        printf("syntax: add-nbo <file1> <file2>\n");
        return 1;
    }

    FILE *fp1, *fp2;

    fp1 = fopen(argv[1], "rb");
    fp2 = fopen(argv[2], "rb");

    if(fp1 == NULL || fp2 == NULL) {
        printf("Can not open file.\n");
        return 1;
    }

    uint32_t buffer1, buffer2;
    size_t bytes1, bytes2;

    bytes1 = fread(&buffer1, sizeof(uint32_t), 1, fp1);
    bytes2 = fread(&buffer2, sizeof(uint32_t), 1, fp2);
    
    if(!isvalidbytes(bytes1, bytes2)) {
        fclose(fp1);
        fclose(fp2);
        return 1;
    }

    uint32_t num1 = ntohl(buffer1);
    uint32_t num2 = ntohl(buffer2);
    uint32_t sum = num1 + num2;

    printf("%u (0x%x) + %u (0x%x) = %u (0x%x)\n", num1, num1, num2, num2, sum, sum);
    fclose(fp1);
    fclose(fp2);

}