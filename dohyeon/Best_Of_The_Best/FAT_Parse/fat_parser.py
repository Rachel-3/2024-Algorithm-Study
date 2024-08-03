import struct
import sys

def read_bpb(image):
    image.seek(0)
    bpb_data = image.read(36)  # BPB의 앞 부분만 읽음
    bytes_per_sector, sectors_per_cluster, reserved_sectors, num_fats = struct.unpack_from('<HBHB', bpb_data, 11)
    image.seek(36)
    fat_size_32 = struct.unpack_from('<I', image.read(4))[0]
    fat_offset = reserved_sectors * bytes_per_sector
    fat_size_bytes = fat_size_32 * bytes_per_sector
    return fat_offset, fat_size_bytes

def read_fat_table(image, offset, size):
    image.seek(offset)
    fat_data = image.read(size)
    # print(f"FAT Data (첫 16 바이트): {fat_data[:16].hex()}")  # 디버깅을 위한 FAT 데이터 출력
    return struct.unpack_from('<' + 'I' * (size // 4), fat_data)

def follow_clusters(fat_table, start_cluster):
    clusters = []
    cluster = start_cluster
    while cluster < 0x0FFFFFF8:  # FAT32 체인컨디션 확인
        clusters.append(cluster)
        next_cluster = fat_table[cluster] & 0x0FFFFFFF  # 상위 4비트 무시
        # print(f"현재 : {cluster}, 다음 : {next_cluster}")  # 디버깅을 위한 현재 클러스터 출력
        if next_cluster == 0 or next_cluster >= len(fat_table):  # 비정상적인 클러스터인 경우
            break
        cluster = next_cluster
    return clusters

def main():
    if len(sys.argv) != 3:
        print("Usage: ./fat_parser <image_file> <start_cluster>")
        sys.exit(1)

    image_file = sys.argv[1]
    start_cluster = int(sys.argv[2])

    with open(image_file, 'rb') as image:
        # BPB를 읽어 FAT 테이블 오프셋과 크기를 계산
        fat_offset, fat_size = read_bpb(image)

        if fat_size == 0:
            sys.exit(1)

        # FAT 테이블 읽기
        fat_table = read_fat_table(image, fat_offset, fat_size)

        # 클러스터 체인 추ㄱ
        clusters = follow_clusters(fat_table, start_cluster)

        # 결과 출력
        print(" ".join(map(str, clusters)))

if __name__ == "__main__":
    main()
