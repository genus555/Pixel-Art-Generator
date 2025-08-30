from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
import os
from pixelate import pixelate

def check_image(root, image, x, y):
    valid = True
    try:
        if (x or y) <= 0:
            valid = False
            raise Exception("Image is too small")
        elif (x or y) >= (image.size[0] or image.size[1]):
            valid = False
            raise Exception("Image is too big")
    finally:
        if not valid:
            root.destroy()

def open_image(image_path, cwd, image_name):
    root = tk.Tk()
    root.title(image_name)

    try:
        pil_image = Image.open(image_path)
        print(f"Original image size: {pil_image.size}")
        
        image_x = 100
        image_y = 100
        check_image(root, pil_image, image_x, image_y)
        pixel_pil_image = pixelate(pil_image, image_x, image_y)

        tk_image = ImageTk.PhotoImage(pixel_pil_image)

        #Create label widget and paint (pack) onto the root
        image_label = ttk.Label(root, image=tk_image)
        image_label.pack()

        #Reference to image to keep Python garbage collector from deleting it
        image_label.image = tk_image

        def on_key_press(event):
            if event.keysym == 'Escape':
                print("Closing window")
                root.destroy()
            elif event.keysym == 's':
                print("Saving image to output folder")
                if not os.path.exists(f"{cwd}/output"):
                    os.mkdir(f"{cwd}/output")
                pixel_pil_image.save(f"{cwd}/output/pixelated_{image_name}")

        root.bind('<Key>', on_key_press)
    except Exception as e:
        print(f"An error has occured: {e}")
    finally:
        root.mainloop() #Start window loop so it doesn't open and close instantly.
