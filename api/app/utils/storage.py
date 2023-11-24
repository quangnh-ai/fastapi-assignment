import os

def create_path(path_dir: str):
    if os.path.exists(path_dir):
        pass
    else:
        os.mkdir(path_dir)

def upload_file_bytes(file_bytes: bytes, path: str):
    f = open(path, "wb")
    f.write(file_bytes)
    f.close()