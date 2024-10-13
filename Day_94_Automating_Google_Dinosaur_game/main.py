import pyautogui
import numpy as np
import time
from PIL import ImageGrab


def restart_game():
    """Simulates pressing the space key to start or restart the game."""
    pyautogui.press('space')


def get_game_region():
    """Returns the region of the game on the screen."""

    return (100, 100, 800, 300)  # (left, top, right, bottom)


def get_game_image(game_region):
    """Captures and returns the game area as a numpy array."""
    screenshot = ImageGrab.grab(bbox=game_region)
    return np.array(screenshot.convert('L'))  # Convert to grayscale


def detect_obstacle(current_frame, previous_frame):
    """Detects obstacles by comparing the current frame with the previous one."""

    watch_area = current_frame[100:150, 100:300]  # Adjust these values based on your game
    prev_watch_area = previous_frame[100:150, 100:300]

    diff = np.abs(watch_area.astype(int) - prev_watch_area.astype(int))

    return np.sum(diff) > 1000  # Adjust this threshold based on testing


def jump():
    """Simulates a jump by pressing the space key."""
    pyautogui.press('space')


def main():
    print("Starting the Chrome Dino game automation...")
    time.sleep(2)  # Wait a few seconds to switch to the game window
    game_region = get_game_region()
    restart_game()  # Start the game

    previous_frame = get_game_image(game_region)
    jump_cooldown = 0

    while True:
        current_frame = get_game_image(game_region)

        if detect_obstacle(current_frame, previous_frame) and jump_cooldown == 0:
            jump()
            jump_cooldown = 10  # Prevent jumping again for a short period

        if jump_cooldown > 0:
            jump_cooldown -= 1

        previous_frame = current_frame
        time.sleep(0.01)  # Short delay to control the script's speed


if __name__ == "__main__":
    main()
