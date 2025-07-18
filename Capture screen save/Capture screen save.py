import os
import pyautogui

MY_PATH = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = "Screen.png"
PATH_SCREEN = os.path.join(MY_PATH, FILE_NAME)


def main():
    image = pyautogui.screenshot(imageFilename=PATH_SCREEN)
    image.save(PATH_SCREEN)
    image.show()
    print(f"new Screen data{image}")
    print("Screen is saved.")


if __name__ == "__main__":
    main()
