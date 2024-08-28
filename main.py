import pyautogui
import time
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--action', type=int, help='Action to perform')
    action = parser.parse_args().action

    if not action:
        action = int(input("Select action:\n1. Start\n2. Check mouse position\n\n> "))

    if action == 2:
        # check mouse position
        try:
            while True:
                # current mouse position
                x, y = pyautogui.position()
                print(f"Mouse position: ({x}, {y})")
                time.sleep(1)
        except KeyboardInterrupt:
            print("Program stopped.")

    if action == 1:
        click_target = int(input("Click target : "))
        # FIX position
        target_x = -1183
        target_y = 453

        interval = 0.1

        # wait before start
        time.sleep(1)

        for i in range(click_target):
            pyautogui.click(target_x, target_y)
            time.sleep(interval)

        print("Auto-clicking completed.")

if __name__ == '__main__':
    # print("""""")
    main()



