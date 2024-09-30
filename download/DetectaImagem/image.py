import pyautogui
import time

procurar = 'sim'

while procurar == "sim":
            try: 
            img = pyautogui.locateCenterOnScreen('img.png')
            pyautogui.click(img.x, img.y)
            time.sleep(1)
            except:
            time.sleep(1)
            print('Não Encontrei')

