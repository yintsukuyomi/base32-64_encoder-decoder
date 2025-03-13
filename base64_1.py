import base64
import tkinter as tk
from tkinter import messagebox

def encode_text(base):
    text = entry_text.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Warning", "Please enter text to encode.")
        return
    if base == 64:
        encoded_bytes = base64.b64encode(text.encode("utf-8"))
    else:
        encoded_bytes = base64.b32encode(text.encode("utf-8"))
    entry_result.delete("1.0", tk.END)
    entry_result.insert(tk.END, encoded_bytes.decode("utf-8"))

def decode_text(base):
    text = entry_text.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Warning", "Please enter Base text to decode.")
        return
    try:
        if base == 64:
            decoded_bytes = base64.b64decode(text.encode("utf-8"))
        else:
            decoded_bytes = base64.b32decode(text.encode("utf-8"))
        entry_result.delete("1.0", tk.END)
        entry_result.insert(tk.END, decoded_bytes.decode("utf-8"))
    except Exception as e:
        messagebox.showerror("Error", "Invalid Base input.")

def copy_result():
    text = entry_result.get("1.0", tk.END).strip()
    if text:
        root.clipboard_clear()
        root.clipboard_append(text)
        root.update()
        messagebox.showinfo("Copied", "Result copied to clipboard.")

root = tk.Tk()
root.title("Base Encoder/Decoder")
root.geometry("500x450")
root.config(bg="#121212")

label_text = tk.Label(root, text="Enter text:", font=("Helvetica", 12), bg="#121212", fg="#BB86FC")
label_text.grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_text = tk.Text(root, height=5, width=50, bg="#1E1E1E", fg="white", insertbackground="white")
entry_text.grid(row=1, column=0, padx=10, pady=10, columnspan=3)

frame_encode_decode = tk.Frame(root, bg="#121212")
frame_encode_decode.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

button_encode_64 = tk.Button(frame_encode_decode, text="Encode Base64", font=("Helvetica", 12), bg="#BB86FC", fg="black", command=lambda: encode_text(64))
button_encode_64.grid(row=0, column=0, padx=5, pady=5)

button_decode_64 = tk.Button(frame_encode_decode, text="Decode Base64", font=("Helvetica", 12), bg="#03DAC6", fg="black", command=lambda: decode_text(64))
button_decode_64.grid(row=0, column=1, padx=5, pady=5)

button_encode_32 = tk.Button(frame_encode_decode, text="Encode Base32", font=("Helvetica", 12), bg="#BB86FC", fg="black", command=lambda: encode_text(32))
button_encode_32.grid(row=1, column=0, padx=5, pady=5)

button_decode_32 = tk.Button(frame_encode_decode, text="Decode Base32", font=("Helvetica", 12), bg="#03DAC6", fg="black", command=lambda: decode_text(32))
button_decode_32.grid(row=1, column=1, padx=5, pady=5)

label_result = tk.Label(root, text="Result:", font=("Helvetica", 12), bg="#121212", fg="#BB86FC")
label_result.grid(row=3, column=0, padx=10, pady=10, sticky="w")
entry_result = tk.Text(root, height=5, width=50, bg="#1E1E1E", fg="white", insertbackground="white")
entry_result.grid(row=4, column=0, padx=10, pady=10, columnspan=3)

button_copy = tk.Button(root, text="Copy", font=("Helvetica", 12), bg="#FBC02D", fg="black", command=copy_result)
button_copy.grid(row=5, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

root.mainloop()
