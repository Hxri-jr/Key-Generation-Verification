import hashlib
import tkinter as tk

def generate_key(email):
    hashed = hashlib.sha256(email.encode()).hexdigest()
    key = hashed[:16]
    key_formatted = '-'.join([key[i:i+4] for i in range(0, len(key), 4)])
    return key_formatted.upper()

def verify_key(email, key):
    generated_key = generate_key(email)
    if generated_key == key:
        return "Verification successful"
    else:
        return "Verification failed"

def verify_key_gui():
    email = email_entry.get()
    key = key_entry.get()
    verification_status_label.config(text=verify_key(email, key))

root = tk.Tk()
root.title("Key Verification")

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

key_label = tk.Label(root, text="Enter the 16-digit key:")
key_label.pack()

key_entry = tk.Entry(root)
key_entry.pack()

verify_button = tk.Button(root, text="Verify Key", command=verify_key_gui)
verify_button.pack()

verification_status_label = tk.Label(root, text="")
verification_status_label.pack()

root.mainloop()
