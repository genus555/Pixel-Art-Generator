import os
from image_handler import open_image

def main ():
    pic = input("What is the file name of your image?\n")
    file_type = input("What is the file suffix (Supported types: png, jpg, jpeg)\n")

    cwd = os.getcwd()
    image_path_exists = os.path.exists(f"{cwd}/pictures/{pic}.{file_type}")
    
    if file_type == ('png' or 'jpg' or 'jpeg'):
        if image_path_exists:
            image_name = f"{pic}.{file_type}"
            image_path = os.path.abspath(f"{cwd}/pictures/{image_name}")
            print("Found image")
            open_image(image_path, cwd, image_name)
        else:
            raise FileNotFoundError("File not found")
    else:
        raise Exception("Not supported File type")

main()