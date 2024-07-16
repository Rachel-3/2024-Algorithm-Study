'''
Author : pental (Kim-Do-Hyeon / BoB 13th 김도현 4048)
Github : https://github.com/kim-do-hyeon
Email : pental@kakao.com
Tel : +82-10-3842-4048
'''
import pyewf
import pytsk3
import os
import hashlib
import argparse
import sys

class EWFImgInfo(pytsk3.Img_Info):
    def __init__(self, ewf_handle):
        self.ewf_handle = ewf_handle
        super(EWFImgInfo, self).__init__(url="", type=pytsk3.TSK_IMG_TYPE_EXTERNAL)

    def close(self):
        self.ewf_handle.close()

    def read(self, offset, size):
        self.ewf_handle.seek(offset)
        return self.ewf_handle.read(size)

    def get_size(self):
        return self.ewf_handle.get_media_size()

def open_e01_image(image_path):
    try:
        filenames = pyewf.glob(image_path)
        ewf_handle = pyewf.handle()
        ewf_handle.open(filenames)
        return ewf_handle
    except Exception as e:
        print(f"Error opening E01 image: {e}")
        sys.exit(1)

def calc_files_with_md5(ewf_handle, output_dir, hash_lists):
    ewf_img_info = EWFImgInfo(ewf_handle)
    try :
        volume = pytsk3.FS_Info(ewf_img_info)
        root_dir = volume.open_dir(path="/")

        for entry in root_dir:
            if entry.info.name.name in [b'.', b'..']:
                continue
            extract_file_with_hash(entry, output_dir, hash_lists)
    except Exception as e:
        print("PROCESSING ERROR!")
        print(e)


def extract_file_with_hash(entry, output_dir, hash_lists):
    try:
        if entry.info.meta.type == pytsk3.TSK_FS_META_TYPE_REG:
            filepath = os.path.join(output_dir, entry.info.name.name.decode())
            file_object = entry
            file_data = file_object.read_random(0, file_object.info.meta.size)
            md5_hash = hashlib.md5(file_data).hexdigest()
            if md5_hash.upper() in hash_lists:
                print(f"HASH {md5_hash} FOUND! File Name : {filepath}")
                with open(filepath, 'wb') as output_file:
                    output_file.write(file_data)
    except Exception as e:
        print(f"Error extracting file {entry.info.name.name.decode()}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Extract files from E01 image and check MD5 hashes")
    parser.add_argument("image_path", help="Path to the E01 image file")
    parser.add_argument("output_dir", help="Directory to save extracted files")
    parser.add_argument("hash_file", help="File containing list of MD5 hashes to check")

    args = parser.parse_args()

    if not os.path.exists(args.image_path):
        print(f"Error: E01 image file '{args.image_path}' does not exist.")
        sys.exit(1)

    if not os.path.isdir(args.output_dir):
        print(f"Error: Output directory '{args.output_dir}' does not exist.")
        sys.exit(1)

    if not os.path.isfile(args.hash_file):
        print(f"Error: Hash file '{args.hash_file}' does not exist.")
        sys.exit(1)

    with open(args.hash_file, "r") as f:
        hash_lists = f.readlines()
    hash_lists = [hash.strip().upper() for hash in hash_lists]

    ewf_handle = open_e01_image(args.image_path)
    calc_files_with_md5(ewf_handle, args.output_dir, hash_lists)

if __name__ == "__main__":
    main()
