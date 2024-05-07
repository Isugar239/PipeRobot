#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.nxtdevices import (LightSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
'''
Project: робот для перемещения, обследования и визуализации труб. Основной и единственный робот
Programmer: Ivan Zakharov, constructor: Eric Kovalev
'''
ev3 = EV3Brick() #for fast request
color = LightSensor(Port.S1) #for fast request
motorA = Motor(Port.A) #for fast request
motorB = Motor(Port.B) #for fast request
motorC = Motor(Port.C) #for fast request
motorD = Motor(Port.D) #for fast request
ev3.speaker.set_speech_options(language="en")
sk = 86 #Hole value
f = open("data.txt", "w") #file request
ev3.speaker.play_file("ready.wav") 
ev3.speaker.set_volume(15, which='_all_')
motorA.reset_angle(0)
def read(): #read the current truba
    alpha = 0 #virtual motorA angle
    for i in range(1, 26):
        motorA.run(300)
        s = color.reflection() #for fast request
        alpha += 36
        while motorA.angle() < alpha:
            wait(1)
        ev3.speaker.beep()
        if s > sk:
            f.write(str(1)) 
        else 
            f.write(str(0))

    while motorA.angle() > 0:
        motorA.run(-550)
    motorA.reset_angle(0)
    alpha = 0
    for i in range(26, 51):
        motorA.run(-300)
        s = color.reflection()
        alpha -= 36
        while motorA.angle() > alpha:
            wait(1)
        ev3.speaker.beep()
        if s > sk:
            f.write(str(1)) 
        else 
            f.write(str(0)) 

    while motorA.angle() < 0:
        motorA.run(550)
    motorA.stop()
    f.write("\n")
    ev3.speaker.play_file("ready.wav")  
eMAX = 300
v = 700
for i in range(1, 2):
    wait(250)
    while motorB.angle() < eMAX:
        motorB.run(v), motorC.run(v), motorD.run(v)
        print(motorB.angle())
        wait(200)
        motorB.run(0), motorC.run(0), motorD.run(0)
        read()
    print("last" + str(color.reflection()))
    ev3.speaker.beep()
v = -700
motorB.run(v), motorC.run(v), motorD.run(v)
while motorB.angle() > 30:
    wait(1)
motorB.run(0), motorC.run(0), motorD.run(0)
f.close()
with open('data.txt', 'r+') as f:
    len = len(f.readlines())
    print(len)
    for i in range(1, len+1):
        f.seek(0, i-1)
        number = f.readline()
        first = number[:25]
        second = number[25:50]
        new = first + second[::-1]
        with open('file.txt', 'a+') as fo:
            fo.write(new+'\n')
