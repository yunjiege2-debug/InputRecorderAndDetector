import pyautogui
import time

print("=== Current Mouse Position Monitor ===")
print("Press Ctrl + C to stop")

while True:
    time.sleep(1)
    x, y = pyautogui.position()
    print(f"Mouse Coordinates -> X: {x:4d}   Y: {y:4d}")