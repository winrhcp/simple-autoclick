import time

import keyboard
import mss
import pygetwindow as gw
import pyautogui


class Logger:
    def __init__(self, prefix=None):
        self.prefix = prefix

    def log(self, data: str):
        if self.prefix:
            print(f"{self.prefix} {data}")
        else:
            print(data)

    def input(self, text: str):
        if self.prefix:
            return input(f"{self.prefix} {text}")
        else:
            return input(text)


class AutoClicker:
    def __init__(self, window_title, click_target, logger):
        self.window_title = window_title
        self.logger = logger
        self.running = False
        self.iteration_count = 0
        self.click_target = click_target

    @staticmethod
    def click_at(x, y):
        pyautogui.click(x, y)

    def toggle_script(self):
        self.running = not self.running
        r_text = "on" if self.running else "off"
        self.logger.log(f'Status changed: {r_text}')

    def click(self):
        windows = gw.getWindowsWithTitle(self.window_title)
        if not windows:
            self.logger.log(
                f"No window found with title: {self.window_title}. Open the Blum web application and restart the script")
            return
        print(windows[0])
        window = windows[0]
        for w in windows:
            if w.left > 0:
                window = w
                break
        
        print(window)
        if window.isMinimized:
            window.restore() # Restore the window if it is minimized.
        window.activate()

        click_count = 0
        with mss.mss() as sct:
            grave_key_code = 41
            keyboard.add_hotkey(grave_key_code, self.toggle_script)
            while True:
                if click_count >= self.click_target:
                        break
                if self.running:
                    monitor = {
                        "top": window.top,
                        "left": window.left,
                        "width": window.width,
                        "height": window.height
                    }
                    cX = monitor["left"] + monitor["width"] // 2
                    cY = monitor["top"] + monitor["height"] // 2
                    self.click_at(cX, cY)
                    click_count += 1
                    self.logger.log(f'Clicked count: {click_count}')

                    time.sleep(0.1)


if __name__ == "__main__":
    logger = Logger("[Auto Click] : ")
    logger.log("Welcome to the free script - autoclicker for the game...")
    click_target = 0
    answer = None
    while answer is None:
        answer = int(input("Click target : "))
        click_target = answer

    logger.log('After starting the mini-game, press the "`" key on the keyboard')
    auto_clicker = AutoClicker("TelegramDesktop", click_target, logger)
    try:
        auto_clicker.click()
    except Exception as e:
        logger.log(f"An error occurred: {e}")
    for i in reversed(range(5)):
        i += 1
        print(f"The script will terminate in {i} seconds")
        time.sleep(1)