import winsound
import time

while True:
    for _ in range(5):
        winsound.Beep(1000, 200)
        time.sleep(0.2)