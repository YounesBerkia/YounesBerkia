from pynput import mouse
from playsound import playsound

def on_click(x, y, button, pressed):
    if pressed:
        playsound('/home/price/Python Code/press.wav')
    else:
        playsound('/home/price/Python Code/unpress.wav')


with mouse.Listener(
        on_click=on_click
) as listener:
    listener.join()
