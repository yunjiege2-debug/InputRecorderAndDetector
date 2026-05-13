import pyautogui
import time

TARGET_X = 1157
TARGET_Y = 1185

CLICK_INTERVAL = 1
TOTAL_CLICKS = 300

print(f"Starting auto-click at ({TARGET_X}, {TARGET_Y})")
print("Starting in 3 seconds...")
time.sleep(3)

pyautogui.FAILSAFE = True

for i in range(TOTAL_CLICKS):
    pyautogui.click(TARGET_X, TARGET_Y)
    print(f"Click {i+1} -> Coordinates ({TARGET_X}, {TARGET_Y})")
    time.sleep(CLICK_INTERVAL)

print("Task complete.")