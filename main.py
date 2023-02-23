import time
import pydirectinput

TOTAL_MATCHES = 0

def match():
    print(f"Starting Match {TOTAL_MATCHES}")
    pydirectinput.moveTo(1660, 1275) # Move the mouse to the x, y coordinates to the "end turn" button
    for i in range(7):
        for j in range(15):
            time.sleep(2)
            pydirectinput.click() 


def loop():
        while True:
            pydirectinput.moveTo(1300, 1100) # Moves the mouse to the play button
            pydirectinput.click()
            time.sleep(8)
            match()
            time.sleep(5)
            pydirectinput.moveTo(1300, 1275) # Moves the mouse to the "Main" button
            pydirectinput.click() 
            global TOTAL_MATCHES
            TOTAL_MATCHES += 1
            time.sleep(1)



def main():
    loop()



if __name__ == "__main__":
    # pydirectinput.moveTo(1300, 1100) # Move the mouse to the x, y coordinates to the "end turn" button
    main()
    #match()