from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
import os
from pixelate import pixelate
from image import ImageObj

def check_image(root, image):
    valid = True
    try:
        if image.x <= 0 or image.y <= 0:
            valid = False
            raise Exception("Image is too small")
        elif image.x >= image.image.size[0] or image.y >= image.image.size[1]:
            valid = False
            raise Exception("Image is too big")
    finally:
        if not valid:
            root.destroy()

def new_root(image, cwd):
    root = tk.Tk()
    root.title(image.image_name)

    try:
        tk_image = ImageTk.PhotoImage(image.pixel_image)

        image_label = ttk.Label(root, image=tk_image)
        image_label.pack()

        def update_image():
            tk_image = ImageTk.PhotoImage(image.pixel_image)

            image_label.configure(image=tk_image)
            image_label.image = tk_image

        def on_key_press(event):
            #print("EVENT:", event.keysym, repr(event.char))
            if event.keysym == 'Escape':
                print("Closing window")
                root.destroy()
            elif event.keysym == 's':
                print("Saving image to output folder")
                if not os.path.exists(f"{cwd}/output"):
                    os.mkdir(f"{cwd}/output")
                image.pixel_image.save(f"{cwd}/output/{image.x}x{image.y}_{image.image_name}")
            elif event.keysym == '.' or event.keysym == 'period':
                print("Increasing by 50 pixels")
                image.x += 50
                image.y += 50
                check_image(root, image)
                image.pixel_image = pixelate(image)
                update_image()
            elif event.keysym == ',' or event.keysym == 'comma':
                print("Decreasing by 50 pixels")
                image.x -= 50
                image.y -= 50
                check_image(root, image)
                image.pixel_image = pixelate(image)
                update_image()
            elif event.keysym == '>' or event.keysym == 'greater':
                print("Increasing by 100 pixels")
                image.x += 100
                image.y += 100
                check_image(root, image)
                image.pixel_image = pixelate(image)
                update_image()
            elif event.keysym == '<' or event.keysym == 'less':
                print("Decreasing by 100 pixels")
                image.x -= 100
                image.y -= 100
                check_image(root, image)
                image.pixel_image = pixelate(image)
                update_image()

        update_image()
        root.bind('<Key>', on_key_press)
    except Exception as e:
        print(f"An error has occured: {e}")
    finally:
        return root


def open_image(image_path, cwd, image_name):
    pil_image = Image.open(image_path)
    print(f"Original image size: {pil_image.size}")

    image = ImageObj(pil_image, image_name, 100, 100)
    image.pixel_image = pixelate(image)
    root = new_root(image, cwd)
    check_image(root, image)

    root.mainloop()
