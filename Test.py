import tkinter as tk
from PIL import Image, ImageTk
import random

# Function to update the GIF frames and handle movement
def update_gif(ind):
    if ind >= frame_count[current_gif]:
        ind = 0  # Reset index if it exceeds the number of frames

    frame = gif_frames[current_gif][ind]
    label.configure(image=frame)
    label.image = frame  # Keep a reference to prevent garbage collection

    ind += 1

    # Move left if gif3 is displayed
    if current_gif == 'gif3.gif':
        move_left()
    # Move right if gif4 is displayed
    elif current_gif == 'gif4.gif':
        move_right()

    root.after(100, update_gif, ind)

# Function to set a random GIF every 5 seconds
def switch_gif():
    global current_gif
    current_gif = random.choice(gif_files)
    update_gif(0)  # Start from the first frame of the new GIF
    root.after(5000, switch_gif)  # Schedule the next GIF switch after 5000 ms (5 seconds)

# Function to move the label left
def move_left():
    x = label.winfo_x() - 5  # Move 5 pixels left
    if x < 0:  # Reset to the right side if it moves off-screen
        x = root.winfo_width() - label.winfo_width()
    label.place(x=x, y=label.winfo_y())

# Function to move the label right
def move_right():
    x = label.winfo_x() + 5  # Move 5 pixels right
    if x > root.winfo_width() - label.winfo_width():  # Reset to the left side if it moves off-screen
        x = 0
    label.place(x=x, y=label.winfo_y())

# Initialize transparent tkinter window
root = tk.Tk()
root.title("Desktop Pet")
root.geometry("400x200")  # Set window size to fit GIFs

# Set the transparent color
transparent_color = "#1c1c1c"  # This color will be made transparent

# Set window attributes for transparency
root.config(bg=transparent_color)  # Set background color to the transparent color
root.wm_attributes('-transparentcolor', transparent_color)  # Make the color transparent
root.wm_attributes('-topmost', True)  # Keep window on top
root.overrideredirect(True)  # Remove window borders

# Load GIFs and their frames
gif_files = ['gif1.gif', 'gif2.gif', 'gif3.gif', 'gif4.gif']
gif_frames = {}
frame_count = {}

for gif in gif_files:
    img = Image.open(gif)
    frames = []
    try:
        while True:
            frames.append(ImageTk.PhotoImage(img.copy()))
            img.seek(img.tell() + 1)
    except EOFError:
        pass
    gif_frames[gif] = frames
    frame_count[gif] = len(frames)

# Set a random GIF initially
current_gif = random.choice(gif_files)

# Create a label to display the GIF with transparent background
label = tk.Label(root, bg=transparent_color)  # Use the same transparent color
label.place(x=200, y=100)  # Start in the middle of the window

# Start the initial GIF and set up the 5-second switch
switch_gif()

# Run the tkinter main loop
root.mainloop()