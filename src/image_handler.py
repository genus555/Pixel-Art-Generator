from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk

def open_image(image_path, cwd, image_name):
    image_y = 50
    image_x = 50
    root = tk.Tk()
    root.title(image_name)

    try:
        pil_image = Image.open(image_path)
        tk_image = ImageTk.PhotoImage(pil_image)

        #Create label widget and paint (pack) onto the root
        image_label = ttk.Label(root, image=tk_image)
        image_label.pack()

        #Reference to image to keep Python garbage collector from deleting it
        image_label.image = tk_image

        def close_on_esc(event):
            if event.keysym == 'Escape':
                root.destroy()

        root.bind('<Escape>', close_on_esc)
    except Exception as e:
        print(f"An error has occured: {e}")
    finally:
        root.mainloop() #Start window loop so it doesn't open and close instantly.
