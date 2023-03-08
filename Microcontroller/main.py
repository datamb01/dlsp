import machine
from machine import Timer
from machine import I2C

from vector3d import Vector3d
from imu import MPU6050

import usocket as socket

import network
import wifi

import time
import utime
from time import sleep

def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to ' + wifi.ssid)
        wlan.connect(wifi.ssid, wifi.pwd)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())

do_connect()

BUFFER_SIZE = 1024
s = socket.socket()
addrinfos = socket.getaddrinfo('192.168.1.107', 8000)
s.connect(addrinfos[0][4])

i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4), freq=100000)
mpu6050 = MPU6050(i2c)
accel=mpu6050.accel
gyro=mpu6050.gyro
DataCounter = 0

def read_imu(tim):
    global DataCounter
    datastr = '{0:3.5f},{1:3.5f},{2:3.5f}\n'.format(accel.x,accel.y,accel.z)
    s.send(datastr.encode())
    
    DataCounter+=1

tim = Timer(-1)
tim.init(period=10, mode=Timer.PERIODIC, callback=read_imu)

start_time=time.time()

while True:
    end_time=time.time()
    programm_duration=end_time-start_time
    if programm_duration>2700:
        tim.deinit()
        print("Sampling finished")
        print("Number of collected samples", DataCounter)
        time.sleep_ms(100)
        s.close()
        break
