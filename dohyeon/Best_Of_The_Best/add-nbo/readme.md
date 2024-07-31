## BOB 13기 - 이경문 멘토님 - 네트워크 과제

# 과제
32 bit 숫자가 파일에 4바이트의 크기로 저장되어 있다(network byte order). 2개의 파일로부터 숫자를 읽어 들여 그 합을 출력하는 프로그램을 작성하라.

# 실행
```
syntax : add-nbo <file1> <file2>
sample : add-nbo a.bin b.bin

# example
$ echo -n -e \\x00\\x00\\x03\\xe8 > thousand.bin
$ echo -n -e \\x00\\x00\\x01\\xf4 > five-hundred.bin
$ ./add-nbo thousand.bin five-hundred.bin
1000(0x3e8) + 500(0x1f4) = 1500(0x5dc)
```

# 상세
- 4바이트 정수를 처리하기 위해서 uint32_t 형식을 사용한다(stdint.h 파일을 include하면 uint32_t를 사용할 수 있음).

- 파일에서 숫자을 읽기 위해서는 fopen, fread 함수 등을 사용한다. fopen하고 나서 fclose 함수도 호출해 주도록 한다. 관련 함수들의 사용 방법은 검색을 통하여 익힌다.

- 정수 덧셈에서 발생하는 overflow는 무시한다.

- 파일이 제대로 열리지 않는 경우, 파일의 크기가 4바이트보다 작아서 제대로 읽지 못했다고 판단되는 경우 등에 대해서 에러 처리를 할 수 있도록 한다.

# 결과
```
// success
pental:/bob/add-nbo$ ./add-nbo thousand.bin five-hundred.bin
1000 (0x3e8) + 500 (0x1f4) = 1500 (0x5dc)
```
```
// Fail
// test.bin file is 3bytes
pental:/bob/add-nbo$ ./add-nbo thousand.bin test.bin
File size is low..
```
```
// Fail
// Argv is one.
pental:/bob/add-nbo$ ./add-nbo thousand.bin
syntax: add-nbo <file1> <file2>
```

