import datetime 

import time

import msvcrt

from os import system

import winsound


frequency = 2000  # Set Frequency To 2500 Hertz

duration = 500  # Set Duration To 1000 ms == 1 second

center_align_chars=50



set_alarm=False

hour=-1

minute=-1

running=True




while(running):

    if set_alarm:

        set_alarm=False

        system('cls')


        time_now=f'Time Now :  {current_time.hour}:{current_time.minute}'.center(center_align_chars, " ")
    
        print(time_now) 


        print('Set Time For Alarm'.center(center_align_chars, " "))

        print("Enter Negative Number to Disable Alarm".center(center_align_chars, " "))

        hour=int(input('Enter Hour 0-23 '.center(center_align_chars, " ")))

        if hour < 0:
            continue
            

        minute=int(input('Enter Minute 0-59 '.center(center_align_chars, " ")))
        
        


    system('cls')


    print('Alarm Clock'.center(center_align_chars, " "))

    print('CS-101 Semester Project'.center(center_align_chars, " "))

    print('\n')

    print('Class ME-11 B'.center(center_align_chars, " "))

    print('Developed BY Team "ABC"'.center(center_align_chars, " "))

    print('Team Members'.center(center_align_chars, " "))

    print('Huzaifa Irfan ( 285501 )'.center(center_align_chars, " "))


    print('\n')




    current_time = datetime.datetime.now() 

    time_now_string=f'Time Now :  {current_time.hour}:{current_time.minute}:{current_time.second}'.center(center_align_chars, " ")
    
    print(time_now_string) 

    print('Press "c" to set/change Alarm'.center(center_align_chars, " "))

    print('Press "x" to Exit'.center(center_align_chars, " "))


    if hour >= 0:

        print('\n')

        alarm_set_string=f'Alarm Set : {hour}:{minute}'.center(center_align_chars, " ")

        print(alarm_set_string)

        if( (hour == current_time.hour) and (minute == current_time.minute)):
        

            print('Beep Beep Beep'.center(center_align_chars, " "))
            print('Press "s" to stop the alarm'.center(center_align_chars, " "))

            winsound.Beep(frequency, duration)

    
    if msvcrt.kbhit():

        char_pressed=msvcrt.getwche()
        if char_pressed == 'c':
            set_alarm=True

        if char_pressed == 's':
            hour=-1

        if char_pressed == 'x':
            running=False


    time.sleep(1)
    



