#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.nxtdevices import (LightSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
ev3 = EV3Brick()
color = LightSensor(Port.S1)
motorA = Motor(Port.A)
motorB = Motor(Port.B)
motorC = Motor(Port.C)
motorD = Motor(Port.D)
ev3.speaker.set_speech_options(language="en")
i = 0
sk = 66 
f = open("data.txt", "w")
ev3.speaker.play_file("ready.wav") 
ev3.speaker.set_volume(5, which='_all_')
motorA.reset_angle(0)
def read():
    alpha = 0
    for i in range(1, 26):
        motorA.run(300)
        s = color.reflection()
        alpha += 36
        while motorA.angle() < alpha:
            wait(1)
        ev3.speaker.beep()
        if s > sk:
            f.write(str(i) + " ") 

    while motorA.angle() > 0:
        motorA.run(-800)
    motorA.reset_angle(0)
    alpha = 0
    for i in range(26, 51):
        motorA.run(-400)
        s = color.reflection()
        alpha -= 36
        while motorA.angle() > alpha:
            wait(1)
        ev3.speaker.beep()
        if s > sk:
            f.write(str(i)+ " ") 

    while motorA.angle() < 0:
        motorA.run(800)
    motorA.stop()
    f.write("\n")
    ev3.speaker.play_file("ready.wav")  
v = 500

print(color.reflection())
for i in range(1, 2):
    wait(250)
    while motorB.angle() < 200:
        motorB.run(v), motorC.run(v), motorD.run(v)
        print(motorB.angle())
        wait(200)
        motorB.run(0), motorC.run(0), motorD.run(0)
        read()
    ev3.speaker.beep()
v = -700
motorB.run(v), motorC.run(v), motorD.run(v)
while motorB.angle() > 30:
    wait(1)
motorB.run(0), motorC.run(0), motorD.run(0)
f.close()
