import sys
import struct

def format_guid(guid_bytes):
    return f'{guid_bytes[3]:02X}{guid_bytes[2]:02X}{guid_bytes[1]:02X}{guid_bytes[0]:02X}-' \
            f'{guid_bytes[5]:02X}{guid_bytes[4]:02X}-' \
            f'{guid_bytes[7]:02X}{guid_bytes[6]:02X}-' \
            f'{guid_bytes[8]:02X}{guid_bytes[9]:02X}-' \
            f'{guid_bytes[10]:02X}{guid_bytes[11]:02X}{guid_bytes[12]:02X}{guid_bytes[13]:02X}{guid_bytes[14]:02X}{guid_bytes[15]:02X}'

def detect_filesystem(f, start_lba):
    f.seek(start_lba * 512)
    sector = f.read(512)
    if b'NTFS' in sector :
        return "NTFS"
    elif b'FAT32' in sector :
        return "FAT32"
    elif b'FAT16' : 
        return "FAT"
    else:
        return "UNKNOWN"

def read_gpt_info(image_path):
    with open(image_path, "rb") as f:
        f.seek(512)
        gpt_header = f.read(92)
        partition_entry_lba = struct.unpack_from("<Q", gpt_header, 72)[0]
        partition_entry_size = struct.unpack_from("<I", gpt_header, 84)[0]
        num_partition_entries = struct.unpack_from("<I", gpt_header, 80)[0]

        results = []

        for i in range(num_partition_entries):
            partition_entry_offset = partition_entry_lba * 512 + i * partition_entry_size
            f.seek(partition_entry_offset)
            partition_entry = f.read(128)
            partition_type_guid = format_guid(partition_entry[0:16])
            if (partition_type_guid) == "00000000-0000-0000-0000-000000000000" :
                break
            starting_lba = struct.unpack_from("<Q", partition_entry, 32)[0]
            ending_lba = struct.unpack_from("<Q", partition_entry, 40)[0]
            filesystem_type = detect_filesystem(f, starting_lba)
            size = (ending_lba - starting_lba + 1) * 512
            results.append(f"{partition_type_guid.replace('-', '')} {filesystem_type} {starting_lba} {size}")

        return results

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gpt_parser.py <image_file>")
        sys.exit(1)

    image_path = sys.argv[1]
    gpt_info = read_gpt_info(image_path)
    
    for info in gpt_info:
        print(info)
