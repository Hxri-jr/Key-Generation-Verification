import hashlib
import tkinter as tk
import pyperclip

def generate_key(email):
    hashed = hashlib.sha256(email.encode()).hexdigest()
    key = hashed[:16]
    key_formatted = '-'.join([key[i:i+4] for i in range(0, len(key), 4)])
    return key_formatted.upper()

def generate_key_gui():
    email = email_entry.get()
    key = generate_key(email)
    key_label.config(text="Your 16-digit key is: " + key)
    copy_button.config(state='normal')  # enable the copy button

def copy_key():
    key = key_label.cget('text').split(': ')[-1]
    pyperclip.copy(key)

root = tk.Tk()
root.title("Key Generator")

window_width = 700
window_height = 350

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

root.resizable(False, False)

email_label = tk.Label(root, text="Enter your E-Mail ID:")
email_label.pack()

email_entry = tk.Entry(root)
email_entry.pack()

generate_button = tk.Button(root, text="Generate Key", command=generate_key_gui)
generate_button.pack()

key_label = tk.Label(root, text="")
key_label.pack()

copy_button = tk.Button(root, text="Copy Key", command=copy_key, state='disabled')
copy_button.pack()

root.mainloop()


#successfully_done

