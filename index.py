import pyautogui
import time
from screeninfo import get_monitors

# Config
DPI = 30
INCHES_TO_PIXELS = 2 * DPI
MOVE_DURATION = 0.3
DELAY = 1.5
POSITION_TOLERANCE = 10  # px - allows slight jitter before resetting

# Get screen center
monitor = get_monitors()[0]
screen_width = monitor.width
screen_height = monitor.height
center_x = screen_width // 2
center_y = screen_height // 2

# Define up/down positions
up_pos = (center_x, center_y - INCHES_TO_PIXELS)
down_pos = (center_x, center_y + INCHES_TO_PIXELS)

# Track expected position
expected_pos = up_pos

print("Moving cursor up/down. Will auto-correct if moved. Ctrl+C to stop.")
try:
    while True:
        # Get current position
        current_pos = pyautogui.position()

        # If cursor was moved manually, reset to center
        if abs(current_pos[0] - center_x) > POSITION_TOLERANCE or abs(current_pos[1] - center_y) > INCHES_TO_PIXELS + POSITION_TOLERANCE:
            print("Mouse moved manually. Resetting to center...")
            pyautogui.moveTo(center_x, center_y, duration=MOVE_DURATION)
            expected_pos = up_pos
            time.sleep(DELAY)

        # Move to expected position
        pyautogui.moveTo(*expected_pos, duration=MOVE_DURATION)
        time.sleep(DELAY)

        # Toggle next position
        expected_pos = down_pos if expected_pos == up_pos else up_pos

except KeyboardInterrupt:
    print("\n✅ Stopped by user.")
except pyautogui.FailSafeException:
    print("\n❗ Fail-safe triggered! Mouse moved to screen corner.")
