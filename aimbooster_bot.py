import time
import keyboard
import win32api, win32con
import mss
import webbrowser

sct = mss.mss()

# Coordinates of window
x1 = 660
y1 = 370
x2 = 600
y2 = 420

window = {"top": y1, "left": x1, "width": x2, "height": y2}

time.sleep(2)

# Click on the given x,y
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

# Press "q" to stop the script
while keyboard.is_pressed('q') == False:
    # Take screenshot
    image = sct.grab(window)

    for y in range(0, int(y2), 10):
        for x in range(0, int(x2), 10):

            r, g, b = image.pixel(x, y)
            if r == 255 and g == 219 and b == 195:
                click(x+x1, y+y1)
                time.sleep(0.02)