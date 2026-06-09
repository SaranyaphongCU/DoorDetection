
import math
import os
import re
import numpy as np
import cv2
import torch
from PIL import Image
from controller import Robot, Keyboard
from transformers import AutoModelForCausalLM, AutoProcessor 

print("[SYSTEM] Loading NVIDIA LocateAnything-3B model manually... Please wait.")

# Initialize the Robot instance
robot = Robot()
    
# Get the time step of the current world
time_step = int(robot.getBasicTimeStep())
speed = 10
    
# Enable keyboard
keyboard = robot.getKeyboard()
keyboard.enable(time_step)
    
# Initialize motors
# For the official PR2 robot, the wheels are named like this:
left_motor = robot.getDevice("left wheel motor")  # Front Left Wheel
right_motor = robot.getDevice("right wheel motor") # Front Right Wheel
    
# Set motors to velocity control mode (position = infinity)
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

#set camera
camera = robot.getDevice('camera')
if camera:
    camera.enable(time_step)
def print_keyboard_help():
    print("Select the 3D window and use the keyboard:\n")
    print("\n")
    print(" W: forward\n")
    print(" A: turn left\n")
    print(" S: backward\n")
    print(" D: turn right\n")
    print("-------------------------------------------------\n")

def main():

    
    print_keyboard_help()
    
    # Main simulation loop
    while robot.step(time_step) != -1:
        key = keyboard.getKey()
        
        if key != -1:
            # Using bitwise OR with 0x20 is a quick trick to hwsdwaasWSWDsaWDandle both upper/lowercase,
            # or you can just check both explicitly:
            if key == ord('W') or key == ord('w'):
                left_motor.setVelocity(speed)
                right_motor.setVelocity(speed)
            elif key == ord('A') or key == ord('a'):
                left_motor.setVelocity(-speed+5)
                right_motor.setVelocity(speed-5)
            elif key == ord('S') or key == ord('s'):
                left_motor.setVelocity(-speed)
                right_motor.setVelocity(-speed)
            elif key == ord('D') or key == ord('d'):
                left_motor.setVelocity(speed-5)
                right_motor.setVelocity(-speed+5)
        else: 
            left_motor.setVelocity(0)
            right_motor.setVelocity(0)

if __name__ == "__main__":
    main()