
from pyfirmata import Arduino, util
from time import sleep

import pyfirmata

import pyautogui





 
board = Arduino('/dev/ttyUSB0') # Change to your port
# print("Start blinking D13")



# while True:
#     board.digital[13].write(1)
#     sleep(1)
#     board.digital[13].write(0)
#     sleep(1)

PINS = (0, 1, 2, 3,4,5)


it = pyfirmata.util.Iterator(board)
it.start()
 
# Start reporting for defined pins

for pin in PINS:
    board.analog[pin].enable_reporting()
 
# Loop for reading the input. Duration approx. 10 s

sens=50

while True:


    jlx,jly, jlb = board.analog[0].read(), board.analog[1].read(), board.analog[2].read()

    print("Joystick Left")
    print(jlx,jly, jlb)



    try:


        #keyboard movements
        #left joystick

        if jlx > 0.7:

            pyautogui.keyDown('a')
            pyautogui.keyUp('d')

            if jly > 0.7:
                # mouse move left bottom
                # pyautogui.move(-sens, sens)

                pyautogui.keyDown('s')
                pyautogui.keyUp('w')

            elif jly < 0.4:
                # mouse move left top
                # pyautogui.move(-sens, -sens)

                pyautogui.keyDown('w')
                pyautogui.keyUp('s')

            else:
                pyautogui.keyUp('s')
                pyautogui.keyUp('w')



        elif jlx < 0.4:

            pyautogui.keyDown('d')
            pyautogui.keyUp('a')

            if jly > 0.7:
                # mouse move right bottom
                # pyautogui.move(sens, sens)

                pyautogui.keyDown('s')
                pyautogui.keyUp('w')

            elif jly < 0.4:
                # mouse move right top
                # pyautogui.move(sens, -sens)
                
                pyautogui.keyDown('w')
                pyautogui.keyUp('s')

            else:
                pyautogui.keyUp('s')
                pyautogui.keyUp('w')


        
        else:

            pyautogui.keyUp('a')
            pyautogui.keyUp('d')

            
            if jly > 0.7:
                # mouse move bottom
                # pyautogui.move(0, sens)

                pyautogui.keyDown('s')
                pyautogui.keyUp('w')

            elif jly < 0.4:

                # mouse move top
                # pyautogui.move(0, -sens)

                pyautogui.keyDown('w')
                pyautogui.keyUp('s')
            
            else:
                pyautogui.keyUp('s')
                pyautogui.keyUp('w')




        if jlb == 0:
            # pyautogui.click()
            # pyautogui.mouseDown()
            pyautogui.press('shiftleft')

        # elif jlb >0.4:
        #     pyautogui.mouseUp()

    except:
        print('Cant handle keyboard')



















    jrx,jry, jrb = board.analog[3].read(), board.analog[4].read(), board.analog[5].read()

    # print("Joystick Right")
    # print(jrx,jry, jrb)


    mx, my = pyautogui.position()

    # print("Mouse Position")

    # print(mx, my)

    try:


        #mouse movements
        #right joystick

        if jrx > 0.7:


            if jry > 0.7:
                # mouse move left bottom
                pyautogui.move(-sens, sens)

            elif jry < 0.4:
                # mouse move left top
                pyautogui.move(-sens, -sens) 
            
            else:

                # mouse move left
                pyautogui.move(-sens, 0)


        elif jrx < 0.4:

            if jry > 0.7:
                # mouse move right bottom
                pyautogui.move(sens, sens) 

            elif jry < 0.4:
                # mouse move right top
                pyautogui.move(sens, -sens) 
            
            else:
                # mouse move right
                pyautogui.move(sens, 0)

        
        else:

            
            if jry > 0.7:
                # mouse move bottom
                pyautogui.move(0, sens) 

            if jry < 0.4:

                # mouse move top
                pyautogui.move(0, -sens) 



        if jrb == 0:
            # pyautogui.click()
            pyautogui.mouseDown()

        elif jrb >0.4:
            pyautogui.mouseUp()

    except:
        print('Cant handle mouse')



    # sleep(0)
