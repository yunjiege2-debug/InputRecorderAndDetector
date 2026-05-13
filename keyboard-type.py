import keyboard
import time
import random

def write_esc_log():
    with open(logfile, "a", encoding="utf-8") as f:
        f.write("[ESC]\n")

keyboard.add_hotkey("esc", write_esc_log)

dirty_words = ""
logfile = "key_log.txt"

with open(logfile, 'w') as a:
    a.write("")

print("Task start, please locate the target field.")
time.sleep(10)

while True:
    text = dirty_words
    time.sleep(0.2)
    keyboard.write(text, delay=0.05)

    if keyboard.is_pressed("esc"):
        write_esc_log()

    with open(logfile, "r") as f:
        log_content = f.read()

    if "[ESC]" in log_content:
        print("Task finished.")
        break