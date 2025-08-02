import tkinter as tk
import win32api

def check_caps():
    global last_state
    caps_state = win32api.GetKeyState(0x14)

    if caps_state != last_state:  # State changed
        last_state = caps_state
        if caps_state:
            label.config(text="CAPS ON", fg="green")
        else:
            label.config(text="CAPS OFF", fg="red")
        root.deiconify()  # Show window
        root.after(2000, root.withdraw)  # Hide after 2 seconds
    
    root.after(100, check_caps)

root = tk.Tk()
root.overrideredirect(True)        
root.attributes("-topmost", True)  
root.geometry("120x40+100+100")  

label = tk.Label(root, font=("Arial", 12, "bold"), bg="black", fg="white")
label.pack(fill="both", expand=True)

last_state = win32api.GetKeyState(0x14)
root.withdraw()  # Start hidden

check_caps()
root.mainloop()
