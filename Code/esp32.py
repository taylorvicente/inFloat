# Code author: Taylor Vicente
# Last updated: 10/20/2026

## MCU: Seeed XIAO ESP32S3 ##

## Peripherals needed: 
# 1. M5Stack CatM
# 1a. American LTE-M MicroSim
# 2. Survivor Light Board
# 3. 5V MiniBoost
# 4. 400 mAh, 3.7 V Lipo
# 5. Hall Sensor Switch
# ##

## Non-Coding Tasks that help with Coding: 
# 1. TODO Identify exactly what microSIM to use and how to abide by their guidelines
# 2. TODO How does SoC work on ESP32
# 3. TODO Create cheat sheet for CatM functions
# 4. TODO Start project and get it approved at Bechtel
# 5. TODO Finalize Survivor Light LED PCB design
# ##

from time import sleep
from machine import Pin, ADC, PWM

# Pin Output Assignments
CommunicationEnable = Pin(3, Pin.OUT, value=0)

# Pin Input Assignments
BatteryADC = ADC(Pin(1))
HallSense = Pin(2, Pin.IN)
SurvivorLight = PWM(Pin(4), freq=1, duty_u16=0)

# Note that D6 and D7 needs to be used for UART (UART0_TX and UART0_RX respectively)


deploymentDetection = False

# Need to 2 main functions that others depend on
# 1. Battery SoC
# 2. Deployment detection

# TODO: Battery SoC
# Description: Need to check the battery ocassionally when the
# board hasn't been deployed so that the system can notify the
# alert receiver to charge the device when low battery
def BatterySoC():
    SoC = BatteryADC * 2 #V_bat = [(R1+R2) / (R1)] * V_adc
    return SoC

# TODO: Deployment Detection
# Description: Utilize Hall Sensor switch to detect when the
# neodymium magnet moves out of range. Check 5 times per second
def DeploymentDetect():
    if (HallSense)

# TODO: 5V Boost Converter Logic
# Description: Only turn on when deployment is detected, enabling
# the CatM board and the survivor light
def EnableComm():
    if (deploymentDetection):
        global CommunicationEnable
        CommunicationEnable = Pin(3, Pin.OUT, value=1)
        enable = True
        return enable

# TODO: Survivor Light
# Description: Flash 3 survivor lights at 20% duty cycle to
# maximize the duration of the battery
def SurvLight():
    if (deploymentDetection & EnableComm()):
        global SurvivorLight
        SurvivorLight = PWM(Pin(4), freq=1, duty_u16=(65535*0.2)) # 20% duty cycle

# TODO: Alert function
# Description: When called by the main function, this should
# enable the CatM to send the alert as a JSON with the
# location data and letting the user know that they system
# has deployed

# TODO: MCU Main
# Description: Just be checking the SoC occasionally and constantly
# driving power through the hall sensor to detect deployment.
# Once deployment is detected, it should power on the 5V booster
# to start the Survivor light function and also the Alert function.
# Alert function should run until their is confirmation of the alert
# being received.
def main():
    