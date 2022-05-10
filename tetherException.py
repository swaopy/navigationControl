# terminal_controlled_bot_tethered_your_turn

from cyberbot import *

sleep(1000)

print("\nSpeeds are -100 to 100\n")

while(True):
    try:
        vL = int(input("Enter left speed: "))
        vR = int(input("Enter right speed: "))
        ms = int(input("Enter ms to run: "))
    
        bot(18).servo_speed(vL)
        bot(19).servo_speed(-vR)
        sleep(ms)
        bot(18).servo_speed(None)
        bot(19).servo_speed(None)

        print()  

    except:
        print("Error in value entered.")
        print("Please try again. \n")
    
    