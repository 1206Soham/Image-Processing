import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from PIL import Image, ImageTk
import matlab.engine
import threading
import os

# Start MATLAB engine
eng = matlab.engine.start_matlab()
eng.addpath(r'C:\Users\SOHAM\Documents\MATLAB\DIP_Project')  # Update as needed

selected_image_path = ""
output_image_path = "images/temp_imgs/output.jpg"
histogram_image_path = "images/temp_imgs/histogram.jpg"

root = tk.Tk()
root.title("DIP Project GUI")
root.geometry("900x750")

image_label = tk.Label(root)
image_label.pack(pady=10)

progress = ttk.Progressbar(root, orient='horizontal', length=400, mode='determinate')
progress.pack(pady=10)

operation = tk.StringVar()
operation.set("Select Operation")

operation_menu = ttk.Combobox(root, textvariable=operation, values=[
    "Image Info", "Resize", "Flip", "Negative", "Convert (Gray/Binary)",
    "Noise Filtering", "Gray Level Slicing", "Generate Histogram",
    "Histogram Equalization", "Contrast Stretching", "Thresholding", "Bit Plane Slicing"
])
operation_menu.pack(pady=5)

input_frame = tk.Frame(root)
input_frame.pack(pady=5)
input_entries = {}

def clear_inputs():
    for widget in input_frame.winfo_children():
        widget.destroy()
    input_entries.clear()

def show_inputs(*args):
    clear_inputs()
    selected = operation.get()

    if selected == "Resize":
        tk.Label(input_frame, text="Width:").grid(row=0, column=0)
        input_entries["width"] = tk.Entry(input_frame)
        input_entries["width"].grid(row=0, column=1)

        tk.Label(input_frame, text="Height:").grid(row=1, column=0)
        input_entries["height"] = tk.Entry(input_frame)
        input_entries["height"].grid(row=1, column=1)

    elif selected == "Flip":
        tk.Label(input_frame, text="Direction (horizontal/vertical):").grid(row=0, column=0)
        input_entries["direction"] = tk.Entry(input_frame)
        input_entries["direction"].grid(row=0, column=1)

        tk.Label(input_frame, text="Angle (degrees):").grid(row=1, column=0)
        input_entries["angle"] = tk.Entry(input_frame)
        input_entries["angle"].grid(row=1, column=1)

    elif selected == "Noise Filtering":
        tk.Label(input_frame, text="Type (salt_pepper/gaussian):").grid(row=0, column=0)
        input_entries["filter_type"] = tk.Entry(input_frame)
        input_entries["filter_type"].grid(row=0, column=1)

    elif selected == "Gray Level Slicing":
        tk.Label(input_frame, text="Min Level:").grid(row=0, column=0)
        input_entries["min_level"] = tk.Entry(input_frame)
        input_entries["min_level"].grid(row=0, column=1)

        tk.Label(input_frame, text="Max Level:").grid(row=1, column=0)
        input_entries["max_level"] = tk.Entry(input_frame)
        input_entries["max_level"].grid(row=1, column=1)

    elif selected == "Convert (Gray/Binary)":
        tk.Label(input_frame, text="Mode (gray/binary):").grid(row=0, column=0)
        input_entries["mode"] = tk.Entry(input_frame)
        input_entries["mode"].grid(row=0, column=1)

    elif selected == "Contrast Stretching":
        tk.Label(input_frame, text="Min Threshold (0-255):").grid(row=0, column=0)
        input_entries["min_thresh"] = tk.Entry(input_frame)
        input_entries["min_thresh"].grid(row=0, column=1)

        tk.Label(input_frame, text="Max Threshold (0-255):").grid(row=1, column=0)
        input_entries["max_thresh"] = tk.Entry(input_frame)
        input_entries["max_thresh"].grid(row=1, column=1)

    elif selected == "Thresholding":
        tk.Label(input_frame, text="Threshold (0-255):").grid(row=0, column=0)
        input_entries["threshold"] = tk.Entry(input_frame)
        input_entries["threshold"].grid(row=0, column=1)

    elif selected == "Bit Plane Slicing":
        tk.Label(input_frame, text="Bit Plane (0-7):").grid(row=0, column=0)
        input_entries["bit"] = tk.Entry(input_frame)
        input_entries["bit"].grid(row=0, column=1)

operation.trace('w', show_inputs)

def show_image(img_path):
    img = Image.open(img_path)
    img = img.resize((300, 300))
    tk_img = ImageTk.PhotoImage(img)
    image_label.configure(image=tk_img)
    image_label.image = tk_img

def browse_image():
    global selected_image_path
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg *.bmp *.tiff")])
    if file_path:
        selected_image_path = file_path
        show_image(selected_image_path)

def process_image():
    if not selected_image_path:
        messagebox.showwarning("No image", "Please select an image first.")
        return

    def run():
        progress['value'] = 20
        root.update_idletasks()
        try:
            op = operation.get()
            if op == "Resize":
                w = int(input_entries["width"].get())
                h = int(input_entries["height"].get())
                eng.resize_image(selected_image_path, output_image_path, w, h, nargout=0)

            elif op == "Flip":
                d = input_entries["direction"].get()
                a = float(input_entries["angle"].get())
                eng.flip_image(selected_image_path, output_image_path, d, a, nargout=0)

            elif op == "Noise Filtering":
                ftype = input_entries["filter_type"].get()
                eng.filter_noise(selected_image_path, output_image_path, ftype, nargout=0)

            elif op == "Gray Level Slicing":
                min_l = int(input_entries["min_level"].get())
                max_l = int(input_entries["max_level"].get())
                eng.gray_level_slicing(selected_image_path, output_image_path, min_l, max_l, nargout=0)

            elif op == "Negative":
                eng.negative_image(selected_image_path, output_image_path, nargout=0)

            elif op == "Convert (Gray/Binary)":
                mode = input_entries["mode"].get()
                eng.convert_image(selected_image_path, output_image_path, mode, nargout=0)

            elif op == "Image Info":
                info = eng.get_image_info(selected_image_path, nargout=1)
                messagebox.showinfo("Image Info", info)
                return

            elif op == "Generate Histogram":
                eng.generate_histogram(selected_image_path, nargout=0)
                show_image(histogram_image_path)
                return

            elif op == "Histogram Equalization":
                eng.histogram_equalize(selected_image_path, output_image_path, nargout=0)

            elif op == "Contrast Stretching":
                min_t = int(input_entries["min_thresh"].get())
                max_t = int(input_entries["max_thresh"].get())
                eng.contrast_stretch(selected_image_path, output_image_path, min_t, max_t, nargout=0)

            elif op == "Thresholding":
                thresh = int(input_entries["threshold"].get())
                eng.threshold_image(selected_image_path, output_image_path, thresh, nargout=0)

            elif op == "Bit Plane Slicing":
                bit = int(input_entries["bit"].get())
                eng.bit_plane_slicing(selected_image_path, output_image_path, bit, nargout=0)

        except Exception as e:
            messagebox.showerror("Error", str(e))
            return

        progress['value'] = 100
        root.update_idletasks()
        messagebox.showinfo("Done", "Processing complete.")
        show_image(output_image_path)

    threading.Thread(target=run).start()

def download_output():
    if not os.path.exists(output_image_path):
        messagebox.showwarning("No Output", "Please process an image first.")
        return

    save_path = filedialog.asksaveasfilename(defaultextension=".jpg")
    if save_path:
        img = Image.open(output_image_path)
        img.save(save_path)
        messagebox.showinfo("Saved", f"Saved to: {save_path}")

tk.Button(root, text="Select Image", command=browse_image).pack(pady=5)
tk.Button(root, text="Process", command=process_image).pack(pady=5)
tk.Button(root, text="Download", command=download_output).pack(pady=5)

root.mainloop()
