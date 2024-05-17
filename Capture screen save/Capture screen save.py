import os
import pyautogui

path_screen = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Screen.png")
print(path_screen)


def main():
    image = pyautogui.screenshot(imageFilename=path_screen)
    image.save(path_screen)
    image.show()
    print(image)
    print("Screen is saved.")


if __name__ == "__main__":
    main()
