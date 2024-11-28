import tkinter as tk
from time import strftime

# Function to update the time display
def time():
    current_time = strftime('%H:%M:%S %p')  # 12-hour format with AM/PM
    label.config(text=current_time)
    label.after(1000, time)  # Update every second

# Setting up the main window
root = tk.Tk()
root.title("Digital Clock")

# Styling the label to show the time
label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='cyan')
label.pack(anchor='center')

time()  # Call the function to initiate time display

root.mainloop()
