import os
from time import sleep
import pyautogui as pag
from playsound import playsound

pag.FAILSAFE = True
count = 5

def main():
    while True:
        sleep(2)
        pag.click()

for x in range(5):
    os.system('cls')
    print(str(count))
    count = count-1
    sleep(1)

playsound('noti.mp3')
main()
