# terminal_controlled_bot_tethered_intro

from cyberbot import *

sleep(1000)

print("\nSpeeds are -100 to 100\n")

while(True):
    text = input("Enter left speed: ")
    vL = int(text)

    text = input("Enter right speed: ")
    vR = int(text)

    text = input("Enter ms to run: ")
    ms = int(text)

    bot(18).servo_speed(vL)
    bot(19).servo_speed(-vR)
    sleep(ms)
    bot(18).servo_speed(None)
    bot(19).servo_speed(None)

    print()  
    
    